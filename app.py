from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minigames.db'
db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)


@app.route("/home")
@app.route("/")
def home():
    return render_template('menu/home.html')

@app.route("/news")
def news():
    return render_template('menu/news.html')

@app.route("/games")
def games():
    return render_template('menu/games.html')

@app.route("/snake")
def snake():
    return render_template('/menu/games/snake.html')

@app.route("/tetris")
def tetris():
    return render_template('/menu/games/tetris.html')

@app.route("/labirint")
def labirint():
    return render_template('menu/games/labirint.html')

@app.route("/clicker")
def clicker():
    return render_template('menu/games/clicker.html')

@app.route("/login")
def login():
    return render_template('account/login.html')

@app.route("/registration")
def registration():
    return render_template('account/registration.html')

if __name__ == '__main__':
    app.run(debug=True)