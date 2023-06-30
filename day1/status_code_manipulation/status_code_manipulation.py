from flask import Flask, render_template, jsonify, make_response, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/endpoint", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        # İstekten kullanıcı adı ve şifreyi al
        username = request.form.get("username")
        password = request.form.get("password")

        # Yetkilendirme işlemleri burada gerçekleşir
        if (username == "34f57c97e2d738c4a6f9d4e0f0ab4c3a" and password == "c53c5fe1cc571ecee8e4185e2a642399") or request.status_code == 200:
            # Doğru kullanıcı adı ve şifre girişi durumunda 200 OK yanıtı döndürülür
            response = {
                "success": True,
                "message": "Login successful",
                "data": "Status Code Manipulation simulasyonunu tamamladın"
            }
            status_code = 200
        else:
            # Yanlış kullanıcı adı veya şifre girişi durumunda 404 Not Found yanıtı döndürülür
            response = {
                "success": False,
                "message": "Invalid credentials"
            }
            status_code = 404

        return make_response(jsonify(response), status_code)
    return render_template('endpoint.html')


if __name__ == "__main__":
    app.run(debug=True)
