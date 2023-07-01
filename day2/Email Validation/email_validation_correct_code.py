from flask import Flask, request

app = Flask(__name__)


def validate_email(email):
    import re
    email_regex = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    else:
        return False


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    email = request.form.get('email')
    if email in validate_email(email):
        return 'E-posta adresi geçerli'
    else:
        return 'Geçersiz e-posta adresi'


if __name__ == '__main__':
    app.run(debug=True)
