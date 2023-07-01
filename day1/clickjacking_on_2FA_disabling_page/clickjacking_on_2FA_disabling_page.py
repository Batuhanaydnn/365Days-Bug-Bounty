from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = [
    {"username": "user1", "password": "pass1", "2fa_enabled": True},
    {"username": "user2", "password": "pass2", "2fa_enabled": True},
    {"username": "user3", "password": "pass3", "2fa_enabled": True}
]

# Disable 2FA route


@app.route('/disable_2fa', methods=['GET', 'POST'])
def disable2fa():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = next((u for u in users if u['username'] == username), None)
        if user and user['password'] == password:
            user['2fa_enabled'] = False
            return redirect(url_for('dashboard'))
    return render_template('disable_2fa.html')

# Index route


@app.route('/')
def index():
    return render_template('index.html')

# Dashboard route


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
