from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')

        # Simulated lack of brute-force protection
        if username == 'admin' and password == 'password':
            if verification_code == '123456':
                return 'Authentication successful without proper brute-force protection'

        # Regular login logic...
        return 'Regular login successful'


@app.route('/login', methods=['GET'])
def render_login_form():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()
