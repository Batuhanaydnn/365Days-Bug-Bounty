from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated user data stored in a dictionary
users = {
    'user1': {
        'password': 'password1',
        'email': 'user1@example.com',
        '2fa_enabled': True
    },
    'user2': {
        'password': 'password2',
        'email': 'user2@example.com',
        '2fa_enabled': True
    }
}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and password == users[username]['password']:
        return redirect(url_for('dashboard', username=username))
    else:
        return render_template('login.html', error='Invalid username or password')


@app.route('/dashboard/<username>')
def dashboard(username):
    user = users.get(username)
    if user:
        return render_template('dashboard.html', user=user)
    else:
        return redirect(url_for('index'))


@app.route('/change_password', methods=['POST'])
def change_password():
    username = request.form.get('username')
    new_password = request.form.get('new_password')

    if username in users:
        users[username]['password'] = new_password
        users[username]['2fa_enabled'] = False
        return redirect(url_for('dashboard', username=username))
    else:
        return redirect(url_for('index'))


@app.route('/change_email', methods=['POST'])
def change_email():
    username = request.form.get('username')
    new_email = request.form.get('new_email')

    if username in users:
        users[username]['email'] = new_email
        users[username]['2fa_enabled'] = False
        return redirect(url_for('dashboard', username=username))
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
