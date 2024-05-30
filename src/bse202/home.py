from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
            user = users[username]
            # In a real application, use Flask-Login for session management
            return redirect(url_for("home"))
        else:
            return render_template("views/login.html", message="Invalid credentials. Please try again.")

    return render_template("views/login.html")

# Dummy logout route
@app.route("/logout", methods=["POST"])
def logout():
    # Perform logout actions here
    return "Logged out successfully"

if __name__ == "__main__":
    app.run(debug=True)
