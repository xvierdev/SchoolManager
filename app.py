from flask import Flask, request, render_template, session
from random import randint
import sqlite3

app = Flask(__name__)
app.secret_key = '123deoliveira4'

def init_db():
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                class TEXT,
                password TEXT
        )
    ''')

    cursor.execute('INSERT INTO users (name, class, password) VALUES ("admin","admin","123")')

    conn.commit()
    conn.close()

def valid_entrance():
    name = session['name']
    password = session['password']
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor();
    cursor.execute(f"SELECT * FROM  users WHERE name = '{name}' AND password = '{password}'")
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def initialize_session():
    for variable_name in ['name', 'class']:
        session.setdefault(variable_name, 0)

@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['class'] = request.form['class']
        session['password'] = request.form['password']
        if valid_entrance():
            return render_template('index.html', username=session['name'], uclass=session['class'])
        return 'deu ruim'

@app.route('/')
def login():
    initialize_session()
    init_db()
    return render_template('login.html')

@app.route('/insert', methods=['POST'])
def insert_new_user():
    conn = sqlite3.connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO users (name, class, password) VALUES ("{request.form['user']}","{{request.form['uclass']}}","{{request.form['pass']}}")''')
    conn.commit()
    conn.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
