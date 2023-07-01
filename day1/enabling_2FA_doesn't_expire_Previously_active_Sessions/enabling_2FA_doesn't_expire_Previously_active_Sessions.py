from flask import Flask, render_template, session, redirect, request
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated database of user accounts
users = {
    'user1': {
        'password': 'password1',
        '2fa_enabled': False,
        'session_active': False,
        'session_id': None,
        'session_expiration': None
    },
    'user2': {
        'password': 'password2',
        '2fa_enabled': False,
        'session_active': False,
        'session_id': None,
        'session_expiration': None
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username]['password'] == password:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        session['username'] = username
        users[username]['session_id'] = session_id
        users[username]['session_active'] = True
        users[username]['session_expiration'] = datetime.now() + \
            timedelta(hours=1)
        return redirect('/dashboard')
    else:
        return render_template('index.html', error='Invalid username or password')


@app.route('/dashboard')
def dashboard():
    if 'session_id' in session and 'username' in session:
        session_id = session['session_id']
        username = session['username']
        if session_id == users[username]['session_id'] and datetime.now() < users[username]['session_expiration']:
            users[username]['session_expiration'] = datetime.now() + \
                timedelta(hours=1)
            return render_template('dashboard.html', username=username)
    return redirect('/')


@app.route('/enable_2fa')
def enable_2fa():
    if 'session_id' in session and 'username' in session:
        session_id = session['session_id']
        username = session['username']
        if session_id == users[username]['session_id'] and datetime.now() < users[username]['session_expiration']:
            users[username]['2fa_enabled'] = True
            return redirect('/dashboard')
    return redirect('/')


@app.route('/logout')
def logout():
    if 'session_id' in session and 'username' in session:
        session_id = session['session_id']
        username = session['username']
        if session_id == users[username]['session_id']:
            users[username]['session_id'] = None
            users[username]['session_active'] = False
            users[username]['session_expiration'] = None
            session.pop('session_id', None)
            session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
