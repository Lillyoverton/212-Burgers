from flask import Flask, render_template, g
import sqlite3


app = Flask(__name__)

MENUDB = 'menu.db'

drinks = [
    ['Cola', '$0.99'],
    ['Ginger Ale', '$0.99'],
    ['Beer', '$1.99'],
    ['Coffee', '$1.99']
]

sides = [
    ['Fries', '$1.99'],
    ['Onion Rings', '$1.99'],
    ['Mushrooms', '$1.99'],
    ['Salad', '$1.99']
]

@app.route('/')
def index():
    db = sqlite3.connect(MENUDB)
    print(db)

    burgers = []
    cur = db.execute('SELECT burger,price FROM burgers')
    for row in cur:
        burgers.append(list(row))
    db.close()

    return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)

@app.route('/order')
def order():
    return render_template('order.html')
