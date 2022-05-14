import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # pip install Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
#__file__ is the path of the current file (i.e. basic.py)
#when a module is loaded in python, this file var is built in and that's set to the name of the actual file
#os.path.abspath(os.path.dirname(__file__)) is the path of the directory that contains the current file (e.g) C:\Users\james\Documents\GitHub\python-flask-tutorial\Databases\basic.py
print(f"Path is {basedir}")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db) #Migrate is a class that is used to create migrations

####################################################
class Puppy(db.Model):
    # Manual TABLE NAME
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"