from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import re
from flask import jsonify
from sqlalchemy import inspect
import requests



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_valid(self):
        if not self.password or not self.username:
            return False
        if not re.match("^[a-zA-Z0-9_.-]+$", self.username):
            return False
        return True


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


@app.route('/users', methods=['GET'])
def list_users():
    render_users = [object_as_dict(user) for user in User.query.all()]

    return jsonify(render_users)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            user = User(
                username=request.form['username'], password=request.form['password'])
            if not user.is_valid():
                return render_template('index.html', message="User name or password is invalid")
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

# script insert into db from other api
def insert_user_from_out_side():
    response = requests.get('https://randomuser.me/api/')
    users = [] 
    for user_json in response.json()["results"]:
        user = User(user_json["login"]["username"], user_json["login"]["password"])
        users.append(user)
        db.session.add(user)
    db.session.commit()
    return users

if (__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    with app.app_context():
        db.create_all()
        app.debug = True
        app.run()
