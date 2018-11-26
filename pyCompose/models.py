from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Players:
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.column(db.String(64))
    lastname = db.Column(db.String(64))
    dob = db.Column(db.DateTime)
    favouritegame = db.Column(db.String(64))
    contactnumber = db.Column(db.String(64))
    phonetype = db.Column(db.String(64))
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    def __init__(self, firstname, lastname, dob, contactnumber, phonetype, favouritegame, username,password):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.favouritegame = favouritegame
        self.contactnumber = contactnumber
        self.phonetype = phonetype
        self.username = username
        self.password = password
    
    def is_authenticated(self):
        return True