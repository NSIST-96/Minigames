from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minigames.db'
db = SQLAlchemy(app)


@app.route("/home")
@app.route("/")
def home():
    return render_template('menu/home.html')

@app.route("/about")
def about():
    return render_template('menu/about.html')

@app.route("/games")
def games():
    return render_template('menu/games.html')


if __name__ == '__main__':
    app.run(debug=True)