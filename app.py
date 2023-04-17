#jazelle and Liz
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "my_secret_key"

users = {} 

@app.route('/')
def home():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            error = "Username already exists."
            return render_template('signup.html', error=error)
        users[username] = password
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            error = "Incorrect username or password."
            return render_template('login.html', error=error)
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')
