from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    username = request.args.get('username')
    return render_template('index.html', username=username)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        twp_fa = request.form.get('two_fa_code')

        if username == 'kdeaejriejweofeo2^dsawod31' and password == 'dkjsajlkdjsaıjfwealfje2313sjda29' and twp_fa == '123459':
            return render_template('home.html', username=username)

        else:
            error = 'Invaild credentials'
            return render_template('login.html', error_message=error)

    return render_template('login.html', error_message=None)


if __name__ == '__main__':
    app.run(debug=True)
