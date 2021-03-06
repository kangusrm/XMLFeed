# project/server/models.py


import datetime

from project.server import app, db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.email)


class Data():

    pole = []

    def __init__(self, pocetRadku):
        self.pole = [{} for x in range(pocetRadku)]

    def setData(self, radek, key, value):
        self.pole[radek][key] = value

    def getData(self, radek, key):
        return self.pole[radek][key]

    def __repr__(self):
        return '<Data>'

def prevod(str):
    return str.translate(str.maketrans({"'": r"\'", "\"": r"\""}))