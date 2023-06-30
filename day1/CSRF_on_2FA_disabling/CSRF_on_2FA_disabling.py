from flask import Flask, render_template, request, session

app = Flask(__name__)

# Simulated database
users = {
    'alice': {
        'username': 'alice',
        'password': 'password',
        '2fa_enabled': True
    }
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username]['password'] == password:
        session['username'] = username
        return render_template('dashboard.html', user=users[username])

    return render_template('index.html', message='Invalid username or password')


@app.route('/disable_2fa', methods=['POST'])
def disable_2fa():
    if 'username' not in session:
        return render_template('index.html', message='Please login first')

    username = session['username']
    users[username]['2fa_enabled'] = False

    return render_template('dashboard.html', user=users[username], message='2FA disabled')


if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.run(debug=True)
