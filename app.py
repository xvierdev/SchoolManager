from flask import Flask, request, render_template, session
from random import randint

app = Flask(__name__)
app.secret_key = '123deoliveira4'

def initialize_session():
    for variable_name in ['name', 'class']:
        session.setdefault(variable_name, 0)

@app.route('/home', methods=['POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['class'] = request.form['class']
    return render_template('index.html', username=session['name'], uclass=session['class'])

@app.route('/')
def login():
    initialize_session()
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
