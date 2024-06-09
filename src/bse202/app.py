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

# Dummy cart data
cart_items = [
    {"name": "Item 1", "quantity": 2, "price": 10.0, "total": 20.0},
    {"name": "Item 2", "quantity": 1, "price": 15.0, "total": 15.0}
]

# Sample data for store inventory
products = {
    'action_games': [
        {'name': 'Action Game 1', 'description': 'Description of Action Game 1.'},
        {'name': 'Action Game 2', 'description': 'Description of Action Game 2.'},
        {'name': 'Action Game 3', 'description': 'Description of Action Game 3.'},
        {'name': 'Action Game 4', 'description': 'Description of Action Game 4.'},
        {'name': 'Action Game 5', 'description': 'Description of Action Game 5.'},
    ],
    'sports_games': [
        {'name': 'Sports Game 1', 'description': 'Description of Sports Game 1.'},
        {'name': 'Sports Game 2', 'description': 'Description of Sports Game 2.'},
        {'name': 'Sports Game 3', 'description': 'Description of Sports Game 3.'},
        {'name': 'Sports Game 4', 'description': 'Description of Sports Game 4.'},
        {'name': 'Sports Game 5', 'description': 'Description of Sports Game 5.'},
    ],
    'strategy_games': [
        {'name': 'Strategy Game 1', 'description': 'Description of Strategy Game 1.'},
        {'name': 'Strategy Game 2', 'description': 'Description of Strategy Game 2.'},
        {'name': 'Strategy Game 3', 'description': 'Description of Strategy Game 3.'},
        {'name': 'Strategy Game 4', 'description': 'Description of Strategy Game 4.'},
        {'name': 'Strategy Game 5', 'description': 'Description of Strategy Game 5.'},
    ],
    'role_play_games': [
        {'name': 'Role Play Game 1', 'description': 'Description of Role Play Game 1.'},
        {'name': 'Role Play Game 2', 'description': 'Description of Role Play Game 2.'},
        {'name': 'Role Play Game 3', 'description': 'Description of Role Play Game 3.'},
        {'name': 'Role Play Game 4', 'description': 'Description of Role Play Game 4.'},
        {'name': 'Role Play Game 5', 'description': 'Description of Role Play Game 5.'},
    ],
    'horror_games': [
        {'name': 'Horror Game 1', 'description': 'Description of Horror Game 1.'},
        {'name': 'Horror Game 2', 'description': 'Description of Horror Game 2.'},
        {'name': 'Horror Game 3', 'description': 'Description of Horror Game 3.'},
        {'name': 'Horror Game 4', 'description': 'Description of Horror Game 4.'},
        {'name': 'Horror Game 5', 'description': 'Description of Horror Game 5.'},
    ]
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
    return render_template("views/store.html", products=products)

@app.route("/account")
def account():
    return render_template("views/account.html")

@app.route('/checkout')
def checkout():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items)
    }
    return render_template('views/checkout.html', cart_summary=cart_summary)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        # Handle payment form submission here
        # This function will be responsible for processing the payment details

        # For now, let's redirect to the payment page
        return redirect(url_for('payment'))

    # If it's a GET request, just render the payment page
    return render_template('views/payment.html')

@app.route("/cart")
def cart():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items)
    }
    return render_template("views/cart.html", cart=cart_items, cart_summary=cart_summary)

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
