from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#THIS MAKES THE WARNING MESSAGES GO AWAY.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# give database location. 
app.config['SQL_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
# Class that represents a table in the db, inherit from db and calling model here.

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime,default=datetime.now)