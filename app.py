from flask import Flask, request, render_template, session, redirect
from sqlite3 import connect
import bcrypt

app = Flask(__name__)
app.secret_key = 'secret_key_here' # override this

def init_db():
    conn = connect('mydata.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            class TEXT,
            password TEXT
        )
    ''')

    # Check if the 'admin' user already exists
    cursor.execute("SELECT * FROM users WHERE name = ?", ('admin',))
    result = cursor.fetchone()

    # If the user doesn't exist, insert it
    if not result:
        hashed_password = bcrypt.hashpw('admin'.encode('utf-8'), bcrypt.gensalt())
        cursor.execute('''
            INSERT INTO users (name, class, password)
            VALUES (?, ?, ?)
        ''', ('admin', 'admin', hashed_password))

    conn.commit()
    conn.close()

def valid_entrance():
    name = session['name']
    password = session['password']

    conn = connect('mydata.db')
    cursor = conn.cursor()

    # Retrieve the stored hashed password from the database
    cursor.execute("SELECT password FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()

    if result:
        stored_hash = result[0]
        # Hash the provided password and compare it to the stored hash
        conn.close()
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
    else:
        conn.close()
        return False

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
    conn = connect('mydata.db')
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO users (name, class, password) VALUES ("{request.form['user']}","{{request.form['uclass']}}","{{request.form['pass']}}")''')
    conn.commit()
    conn.close()
    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
