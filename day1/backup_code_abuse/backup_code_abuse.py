from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# User database with hashed passwords and backup codes (insecure storage for simulation purposes)
users = {
    "user1": {
        "password_hash": "hashed_password_1",
        "2fa_enabled": True,
        "backup_codes": [
            "backup_code_1",
            "backup_code_2",
            "backup_code_3"
        ]
    },
    "user2": {
        "password_hash": "hashed_password_2",
        "2fa_enabled": True,
        "backup_codes": [
            "backup_code_4",
            "backup_code_5",
            "backup_code_6"
        ]
    }
}

# Simulated login page


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if authenticate_user(username, password):
            return redirect("/dashboard")
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

# Simulated dashboard page


@app.route("/dashboard")
def dashboard():
    if not is_user_authenticated():
        return redirect("/")
    return render_template("dashboard.html")

# Simulated 2FA disable page


@app.route("/disable_2fa", methods=["GET", "POST"])
def disable_2fa():
    if not is_user_authenticated():
        return redirect("/")

    if request.method == "POST":
        backup_code = request.form.get("backup_code")
        if verify_backup_code(backup_code):
            disable_2fa()
            return redirect("/dashboard")
        else:
            return render_template("disable_2fa.html", error="Invalid backup code")

    return render_template("disable_2fa.html", error="")


def authenticate_user(username, password):
    if username in users and hash_password(password) == users[username]["password_hash"]:
        return True
    return False


def is_user_authenticated():
    # Check user authentication status (e.g., session, token, etc.)
    return True  # For simplicity, assume user is authenticated


def verify_backup_code(backup_code):
    username = get_current_username()
    if username in users and backup_code in users[username]["backup_codes"]:
        return True
    return False


def disable_2fa():
    username = get_current_username()
    if username in users:
        users[username]["2fa_enabled"] = False


def get_current_username():
    # Retrieve current username from session or token
    return "user1"  # For simplicity, assume it's always "user1"


def hash_password(password):
    # Perform password hashing (e.g., using bcrypt)
    # For simplicity, use a fixed hash for demonstration purposes
    return "hashed_password_1"


if __name__ == "__main__":
    app.run(debug=True)
