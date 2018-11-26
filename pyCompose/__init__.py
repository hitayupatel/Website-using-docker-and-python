from flask import Flask,render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from models import Players, db
import os
import datetime as dtime

app = Flask(__name__)
#database connection setting
app.secret_key = os.urandom(20)
db_uri = 'mysql://agsroot:ags@db:3306/project2_db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/game_release")
def game_release():
    #difference in date till countdown
    diff = dtime.datetime(2018, 12, 30) - dtime.datetime.now()
    return render_template("gameRelease.html", days = diff.days)

@app.route("/login")
def login():
    return render_template("login.html")

#login functionality
@app.route("/loginAction", methods = ['GET', 'POST'])
def loginAction():
    if request.method == 'POST':
        usr = request.form['username']
        pwd = request.form['password']
    if usr is not None:
        player = Players.query.filter(Players.username == usr).first()
    if player.password == pwd:
        session['username'] = None
        return render_template("hello.html", username = session['username'])
    else:
        session['username'] = None
        flash("Invalid Username or Password")
        return redirect(url_for('login'))

#register functionality
@app.route("/registerAction", methods=['POST'])
def registerAction():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        dob = request.form['dob']
        fav_game = request.form['favouritegame']
        contactnumber = request.form['phonenumber']
        phonetype = request.form.get('phonetype')
        usrname = request.form['username']
        pwd = request.form['password']
        usr = Players(first_name,last_name,dob, fav_game, contactnumber, phonetype, usrname, pwd)
        db.session.add(usr)
        db.session.commit()
        session['username'] = usrname
    return render_template("home.html", usrname = session['username'])

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')