<h1>
    Chess Master ♚ 
</h1>

## 📋 Tópicos

<div>
 • <a href="#-sobre">Sobre</a> </br>
 • <a href="#-ferramentas">Ferramentas</a> </br>
 • <a href="#-como-executar-o-projeto">Como executar o projeto</a> </br>    
 • <a href="#-licença">Licença</a></br>
</div>

## 📗 Sobre

**ChessMaster** é uma plataforma de estudo de xadrez que utiliza a poderosa engine **Stockfish**. O usuário pode contar com um **assistente virtual** para receber as melhores recomendações durante suas partidas, jogar contra uma **IA de alto desempenho** com **99,9% de precisão** e praticar exercícios focados em diferentes **estilos e estratégias de jogo**.

## ✨ Estágio de desenvolimento

O projeto é dividido em 3 funcionalidades principais: Assitente de xadres em tempo real (ChessGpt), Jogo treino contra IA e Exercícios de prática de xadrez.

**ChessGPT**

Assistente de xadrez que sugere as **melhores** jogadas **durante uma partida** utilizando a engine **Stockfish**. O usuário pode interagir com o sistema para receber recomendações em tempo real, com **99.9% de precisão**.

Essa etapa do desenvolvimento á está concluida utilizando uma interface temporária.

**Jogo vs IA**

...

Essa etapa ainda não está em desenvolvimento, provalvelmente será implementada em uma nova interface mais avançada utilizando React.

**Exercícios**

...

Essa etapa está em desenvolvimento. ...

**Interface**

Atualmente a interface utilizada é desenvolvida em HTML, CSS e JS, tudo em um único arquivo HTML para o foco no desenovlivmento de funcionalidades backend. Essa interface será substituida em breve por uma interface em React.

## 🔧 Ferramentas

### 💻 **Website** ( HTML + CSS + JavaScript )**

- [Google Fonts](https://fonts.googleapis.com/css2?family=Gabarito:wght@400;500;600;700;800;900&display=swap)
- [Font Awesome](https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.cs)

### 🔄 **API** ([Pyhton](https://www.python.org))

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [sqlite3](https://www.sqlite.org/)
- [Chess](https://python-chess.readthedocs.io/en/latest/)
- [OS](https://docs.python.org/3/library/os.html)
- [Secrets](https://docs.python.org/pt-br/3.6/library/secrets.html)

### 🛠️ **Utilitários**

- Base de dados: **[DB Browser](https://sqlitebrowser.org/)**
- Compiladores: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)**

## ▶ Como executar o projeto

- 🌐 **Frontend** (WebSite HTML, CSS, JavaScript)
- ⚙️ **Backend: Api** (Python)
- 🗂️ **Base de dados: Sqlite**

### ⚙️ Backend:

#### Criando um ambiente viradvetual:

1 - Navegue até o diretório onde deseja criar o ambiente virtual:

```bash
 cd /path/to/your/project
```

2 - Crie um ambiente virtual:

```bash
 python3 -m venv name
```

3 - Ative o ambiente virtual:

```bash
 name\Scripts\activate
```

#### Instalação de bibliotecas:

```bash
 pip install flask
```

```bash
 pip install sqlite3
```

```bash
 pip install python-chess
```

```bash
 pip install python-secrets
```

```bash
 pip install python-secrets
```

#### Importação de bibliotecas:

```bash
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
import chess
import chess.engine
import os
import secrets
```

### 🌐 Frontend:

Tratando-se de um estágio de desenvolvimento inicial focado no backend, um arquivo **HTML** é usado como interface, sendo automaticamente reconhecido pelo **Flask** e executado ao executar a **API**.

## 📜 Licença

### Este projeto está sob licença do MIT.

<br>
Desenvolvido por Miguel Marsico 👋🏻
