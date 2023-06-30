from flask import Flask, render_template, request, session, redirect, url_for
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

valid_2fa_code = '123456'
used_2fa_codes = []


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form inputs
        username = request.form.get('username')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')

        # Validate the username and password
        if username == 'admin' and password == 'password':
            # Check the 2FA code
            if verification_code == valid_2fa_code:
                # Check for code reusability vulnerability
                if valid_2fa_code in used_2fa_codes:
                    return 'Authentication successful, but 2FA code already used'

                # Mark the code as used
                used_2fa_codes.append(valid_2fa_code)

                # Store the user's session
                session['username'] = username

                return redirect(url_for('protected'))

            return 'Invalid verification code'

        return 'Invalid username or password'

    return render_template('login.html')


@app.route('/protected')
def protected():
    # Check if the user is authenticated
    if 'username' in session:
        return 'Welcome to the protected area!'
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Clear the user's session
    session.clear()
    return 'Logged out successfully'


if __name__ == '__main__':
    app.run(debug=True)
