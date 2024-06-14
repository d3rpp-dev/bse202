from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import re

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Dummy user for demonstration
class User:
    def __init__(self, username):
        self.username = username
        self.vault_coin = 0  # Initialize vault_coin for each user, this is the users top up balance called Vault Coin - Virtual Vaults digital currency.
        self.top_up_option = 0  # Initialize top_up_option for each user, this is used for the system to understand how much currency the user is trying to top up with

users = {
    "john": User("john"),
    "jane": User("jane")
}

# shopping cart
cart_items = []

# Define global variables
payment_details = {
    'card_number': None,
    'expiry_date': None,
    'cvv': None,
    "payment_method": "Credit Card",
    "total_price": sum(item["total"] for item in cart_items)
}

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

# Define regex patterns
card_number_regex = re.compile(r'^\d{16}$')
expiry_date_regex = re.compile(r'^(0[1-9]|1[0-2])\/([0-9]{4})$')
cvv_regex = re.compile(r'^\d{3,4}$')

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
    if 'username' in session:
        username = session['username']
        current_user = users.get(username)
        if current_user:
            return render_template("views/account.html", current_user=current_user)
        else:
            flash('User not found.', 'error')
            return redirect(url_for('login'))
    else:
        flash('You are not logged in.', 'error')
        return redirect(url_for('login'))

@app.route('/top_up_credit', methods=['GET', 'POST'])
def top_up_credit():
    if request.method == 'POST':
        current_user = users[session['username']]
        amount = current_user.top_up_option
        current_user.vault_coin += amount
        flash(f'Successfully topped up ${amount} via Credit Card.', 'success')
        return redirect(url_for('account'))
    return render_template('views/top_up_credit.html')

@app.route('/voucher', methods=['GET', 'POST'])
def voucher():
    if request.method == 'POST':
        voucher_code = request.form.get('voucher-code')
        if voucher_code == "SAMPLEVOUCHER123":  # Replace with actual voucher validation logic
            current_user = users[session['username']]
            amount = current_user.top_up_option
            current_user.vault_coin += amount
            flash('Voucher successfully applied!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Invalid voucher code. Please try again.', 'error')
            return redirect(url_for('top_up'))  # Corrected redirection

    return render_template('views/voucher.html')


@app.route('/update_top_up_option', methods=['POST'])
def update_top_up_option():
    if 'username' in session:
        username = session['username']
        current_user = users.get(username)
        if current_user:
            data = request.get_json()
            amount = int(data['amount'])
            current_user.top_up_option = amount
            return jsonify({'success': True}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Not logged in'}), 401

@app.route('/top_up', methods=['GET', 'POST'])
def top_up():
    if request.method == 'POST':
        amount_str = request.form.get('amount')
        if amount_str and amount_str.isdigit():
            amount = int(amount_str)
            payment_method = request.form.get('payment')
            current_user = users[session['username']]
            
            current_user.top_up_option = amount

            if payment_method == 'creditCard':
                return redirect(url_for('top_up_credit'))
            elif payment_method == 'voucher':
                return redirect(url_for('voucher'))  # Corrected redirection

            flash('Please select a payment method.', 'error')
        else:
            flash('Invalid amount. Please enter a valid number.', 'error')

    return render_template('views/top_up.html')


@app.route('/checkout')
def checkout():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items)
    }
    return render_template('views/checkout.html', cart_summary=cart_summary)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    global payment_details

    if request.method == 'POST':
        # Handle form submission and validate payment details
        card_number = request.form.get('card_number', '').strip()
        expiry_date = request.form.get('expiry_date', '').strip()
        cvv = request.form.get('cvv', '').strip()

        # Ensure the inputs are strings (they should be if coming from form)
        if not isinstance(card_number, str):
            flash('Invalid card number format.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)
        if not isinstance(expiry_date, str):
            flash('Invalid expiry date format.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)
        if not isinstance(cvv, str):
            flash('Invalid CVV format.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)

        # Validate card number
        if not card_number_regex.match(card_number):
            flash('Invalid card number. Please enter a valid 16-digit card number.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)

        # Validate expiry date
        if not expiry_date_regex.match(expiry_date):
            flash('Invalid expiry date. Please enter a valid date in MM/YYYY format.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)

        # Validate CVV
        if not cvv_regex.match(cvv):
            flash('Invalid CVV. Please enter a valid 3 or 4-digit CVV number.', 'error')
            return render_template('views/payment.html', payment_details=payment_details)
        
        # If all validations pass, update payment details
        payment_details['card_number'] = card_number
        payment_details['expiry_date'] = expiry_date
        payment_details['cvv'] = cvv
        
        # Dummy payment processing logic
        # For now, let's assume the payment is successful
        # Redirect to order summary page after successful payment
        return redirect(url_for('order_summary'))

    # If it's a GET request, just render the payment page
    return render_template('views/payment.html', payment_details=payment_details)

@app.route("/order_summary")
def order_summary():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items)
    }
    return render_template("views/order_summary.html", cart=cart_items, cart_summary=cart_summary, payment_details=payment_details)

@app.route("/cart")
def cart():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items)
    }
    return render_template("views/cart.html", cart=cart_items, cart_summary=cart_summary)

@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_name = request.form.get("product_name")
    # Assume a fixed price for simplicity, well modify to fetch price from the products data
    price = 10.0
    item = next((item for item in cart_items if item["name"] == product_name), None)
    if item:
        item["quantity"] += 1
        item["total"] = item["quantity"] * item["price"]
    else:
        cart_items.append({"name": product_name, "quantity": 1, "price": price, "total": price})
    return redirect(url_for("cart"))

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_name = request.form.get("product_name")
    global cart_items
    cart_items = [item for item in cart_items if item["name"] != product_name]
    return redirect(url_for("cart"))

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
