from flask import Flask, render_template
from time import sleep
import os
from flask_sqlalchemy import SQLAlchemy

#Init flask instance with name argument
app = Flask(__name__)#built in python varaible that refers to the local python file you are working in
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
#Creating an instance of the sql alchemy class I imported
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique = True)
    price = db.Column(db.Integer(), nullable=False )
    barcode = db.Column(db.String(length=12), nullable=False, unique= True)
    description= db.Column(db.String(length = 1024), nullable=False, unique = True)


@app.route('/')
@app.route('/home')
#This is a decorator, when you type in a url without navigating to a specific page it automatically redirects you to this page
def home_page():
    return render_template('home.html')
@app.route('/market')
def market_page():
    items = [
            {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
            {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
            {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
            ]
    return render_template('market.html', items=items)

#Runs the app with debugging for the automatic updating after making changes
app.run(debug=False)
