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


@app.route("/games/snake")
def snake():
    return render_template('menu/snake.html')

@app.route("/games/tetris")
def tetris():
    return render_template('menu/tetris.html')

@app.route("/games/labirint")
def labirint():
    return render_template('menu/labirint.html')

@app.route("/games/clicker")
def clicker():
    return render_template('menu/clicker.html')



if __name__ == '__main__':
    app.run(debug=True)