import os
import datetime
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# instantiate the app

app = Flask(__name__)

#set config

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
print(app.config)

#instantiate the db

db = SQLAlchemy(app)

#model

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.datetime.now()

#routes

@app.route('/ping', methods=['GET'])
def ping_pong():
   print(app.config)
   print("hahaha")
   return jsonify({
       'status': 'success',
       'message': 'pong!'
   })

@app.route('/', methods=['GET'])
def damn():
	return str(app.config)
