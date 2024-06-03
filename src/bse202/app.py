from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Dummy user for demonstration
class User:
    def __init__(self, username):
        self.username = username

users = {
    "john": User("john"),
    "jane": User("jane")
}

@app.route("/")
def home():
    return render_template("views/home.html")

@app.route("/about")
def about():
    return render_template("views/about.html")

@app.route("/contact")
def contact():
    return render_template("views/contact.html")

@app.route("/store")
def store():
    return render_template("views/store.html")

@app.route("/account")
def account():
    return render_template("views/account.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Dummy authentication logic
        if username in users and password == "password":
            # Set the user in the session
            session['username'] = username
            return redirect(url_for("home"))
        else:
            return render_template("views/login.html", message="Invalid credentials. Please try again.")

    return render_template("views/login.html")

@app.route("/logout", methods=["POST"])
def logout():
    # Perform logout actions here
    session.pop('username', None)  # Remove the user from the session
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
