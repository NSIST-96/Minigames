from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minigames.db'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)


@app.route("/home")
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def index():
    return render_template('about.html')

@app.route("/games")
def index():
    return render_template('games.html')


if __name__ == '__main__':
    app.run(debug=True)