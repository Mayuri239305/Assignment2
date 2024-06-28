from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()

def init_app(app):
    mongo.init_app(app)
    bcrypt.init_app(app)

def register_user(username, password):
    password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
    user = {"username": username, "password": password_hash}
    mongo.db.users.insert_one(user)

def validate_user(username, password):
    user = mongo.db.users.find_one({"username": username})
    if user and bcrypt.check_password_hash(user['password'], password):
        return True
    return False

