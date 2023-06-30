from flask import Flask, request, render_template

app = Flask(__name__)

# Simulated user accounts and their associated verification codes
user_accounts = {
    'user1': '123456',
    'user2': '654321',
    'user3': '987654'
}


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')

        if username in user_accounts and password == 'password':
            # Simulated vulnerability: Missing 2FA code integrity validation
            # Any valid verification code is accepted regardless of its association with the user's account
            if verification_code in user_accounts.values():
                return 'Authentication successful without valid 2FA code'

            return 'Invalid verification code'

        return 'Invalid username or password'

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
