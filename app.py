from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minigames.db'
db = SQLAlchemy(app)


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



if __name__ == '__main__':
    app.run(debug=True)