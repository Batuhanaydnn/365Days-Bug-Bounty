# app.py
from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

# Simulated database of user accounts
users = {
    'user1': {
        'password': 'password1',
        '2fa_enabled': True,
        '2fa_code': '',
    },
    'user2': {
        'password': 'password2',
        '2fa_enabled': True,
        '2fa_code': '',
    }
}

# Generate a random 2FA code for each user


def generate_2fa_code():
    return ''.join(random.choices(string.digits, k=6))

# Route for the login page


@app.route('/')
def index():
    return render_template('index.html')

# Route for handling the login form submission


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    code = request.form['code']

    if username in users and users[username]['password'] == password:
        if users[username]['2fa_enabled']:
            # Generate a new 2FA code if the current code is null or "000000"
            if users[username]['2fa_code'] == '' or users[username]['2fa_code'] == '000000':
                users[username]['2fa_code'] = generate_2fa_code()

            # Allow null or "000000" code to bypass 2FA
            if code == '' or code == '000000':
                return redirect('/dashboard')
            elif code == users[username]['2fa_code']:
                return redirect('/dashboard')

        return render_template('index.html', error='Invalid credentials or 2FA code')

# Route for the dashboard page


@app.route('/dashboard')
def dashboard():
    return "Dashboard"


if __name__ == '__main__':
    app.run(debug=True)
