from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minigames.db'
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    snake_record = db.Column(db.Integer)
    tetris_record = db.Column(db.Integer)
    dino_record = db.Column(db.Integer)
    clicker_record = db.Column(db.Integer)


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

@app.route("/dino")
def dino():
    return render_template('menu/games/dino.html')

@app.route("/clicker")
def clicker():
    return render_template('menu/games/clicker.html')

@app.route("/login")
def login():
    return render_template('account/login.html')

@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        account = Account(login, password, 10, 10, 10, 10)

        try:
            db.session.add(account)
            db.session.commit()
            return redirect('account/account.html')
        except:
            return 'При регистрации возникла ошибка. Попробуйте снова.'
    else:
        return render_template('account/registration.html')

@app.route("/account")
def account():
    return render_template('account/account.html')

if __name__ == '__main__':
    app.run(debug=True)