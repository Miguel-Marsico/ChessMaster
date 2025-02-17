from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
import chess
import chess.engine
import os
import secrets

SECRET_KEY = secrets.token_hex(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
DATABASE = 'users.db'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT NOT NULL,
                          email TEXT NOT NULL UNIQUE,
                          password TEXT NOT NULL)''')
        conn.commit()
        conn.close()

init_db()

class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def get(user_id):
        return User._fetch_one("SELECT * FROM users WHERE id = ?", (user_id,))

    @staticmethod
    def find_by_email(email):
        return User._fetch_one("SELECT * FROM users WHERE email = ?", (email,))

    @staticmethod
    def create(username, email, password):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        user = User(cursor.lastrowid, username, email, password)
        conn.close()
        return user

    @staticmethod
    def _fetch_one(query, params):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute(query, params)
        user = cursor.fetchone()
        conn.close()
        if user:
            return User(user[0], user[1], user[2], user[3])
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class ChessGame:
    def __init__(self):
        self.board = chess.Board()
        self.moves_history = []

    def reset(self):
        self.board = chess.Board()
        self.moves_history = []

    def make_move(self, move):
        try:
            uci_move = chess.Move.from_uci(move)
            if uci_move in self.board.legal_moves:
                self.moves_history.append(self.board.copy())
                self.board.push(uci_move)
                return True
            return False
        except Exception:
            return False

    def undo_move(self):
        if self.moves_history:
            self.board = self.moves_history.pop()
            return True
        return False

    def get_best_move(self):
        try:
            with chess.engine.SimpleEngine.popen_uci("stockfish/stockfish-windows-x86-64-avx2.exe") as engine:
                result = engine.play(self.board, chess.engine.Limit(time=2.0))
                return result.move.uci()
        except Exception:
            return None

game = ChessGame()
game.suggested_move = None
playing_white = True

@app.route('/')
def index():
    return render_template('index.html', current_user=current_user)

@app.route('/chessgpt')
@login_required
def chessgpt():
    return render_template('chessgpt.html', current_user=current_user)

@app.route('/start', methods=['POST'])
@login_required
def start_game():
    global playing_white
    game.reset()
    playing_white = request.json['playing_white']
    responses = ["Você vai jogar com as peças brancas." if playing_white else "Você vai jogar com as peças pretas."]
    if playing_white:
        move = game.get_best_move()
        if move:
            game.make_move(move)
            responses.append(f"Primeira jogada sugerida para as Brancas: {move}")
    return jsonify({"responses": responses, "board": game.board.fen()})

@app.route('/move', methods=['POST'])
@login_required
def make_move():
    move_uci = request.json['move']
    responses = []

    if move_uci.lower() == 'undo':
        if game.undo_move():
            responses.append("Jogada desfeita.")
        else:
            responses.append("Não há jogadas para desfazer.")
    else:
        if game.make_move(move_uci):
            if game.board.is_game_over():
                responses.append("Fim do jogo.")
        else:
            responses.append("Movimento inválido. Tente novamente.")

    return jsonify({"responses": responses, "board": game.board.fen()})

@app.route('/confirm_move', methods=['POST'])
@login_required
def confirm_move():
    if game.suggested_move:
        game.make_move(game.suggested_move)
        game.suggested_move = None
        return jsonify({"responses": ["Jogada confirmada."], "board": game.board.fen()})
    return jsonify({"responses": ["Nenhuma jogada para confirmar."], "board": game.board.fen()})

@app.route('/get_suggestion', methods=['GET'])
@login_required
def get_suggestion():
    best_move = game.get_best_move()
    if best_move:
        game.suggested_move = best_move
        return jsonify({"suggested_move": best_move})
    return jsonify({"suggested_move": None})

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.find_by_email(email)
    if user and user.password == password:
        login_user(user)
        return redirect(url_for('index'))
    flash('Login inválido. Verifique seu e-mail e senha.')
    return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    user = User.create(username, email, password)
    login_user(user)
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
