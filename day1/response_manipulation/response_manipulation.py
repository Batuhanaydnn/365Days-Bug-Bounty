from flask import Flask, jsonify, request, render_template
import random
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        two_factor = request.form.get("two_factor")

        if username == 'admin' and password == 'passowrd' and two_factor == str(random.randint(1, 1000000000)):
            response = {
                'success': True,
                'message': 'Login Successful'
            }
        else:
            response = {
                'success': False,
                'message': 'Invaild credentials or 2FA code'
            }

        return jsonify(response)

    return render_template('login.html')


if __name__ == '__main__':
    app.run()
