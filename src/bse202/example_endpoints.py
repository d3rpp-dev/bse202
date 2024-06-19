from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    jsonify,
)
import re


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management


if __name__ == "__main__":
    app.run(debug=True)


# Dummy user for demonstration
class User:
    def __init__(self, username):
        self.username = username
        self.vault_coin = 0  # Initialize vault_coin for each user, this is the users top up balance called Vault Coin - Virtual Vaults digital currency.
        self.top_up_option = 0  # Initialize top_up_option for each user, this is used for the system to understand how much currency the user is trying to top up with


users = {"john": User("john"), "jane": User("jane")}

# shopping cart
cart_items = []

# Define global variables
payment_details = {
    "card_number": None,
    "expiry_date": None,
    "cvv": None,
    "payment_method": "Credit Card",
    "total_price": sum(item["total"] for item in cart_items),
}

# Store product dictionary
products = {
    "action_games": [
        {
            "name": "DOOM Eternal",
            "description": "Experience the ultimate combination of speed and power with the next leap in push-forward, first-person combat.",
            "image": "media/game/action1.jfif",
        },
        {
            "name": "Sekiro: Shadows Die Twice",
            "description": "Carve your own clever path to vengeance in this critically acclaimed adventure from developer FromSoftware.",
            "image": "media/game/action2.jfif",
        },
        {
            "name": "Monster Hunter: World",
            "description": "Battle gigantic monsters in epic locales. As a hunter, you’ll take on quests to hunt monsters in a variety of habitats.",
            "image": "media/game/action3.jfif",
        },
        {
            "name": "Devil May Cry 5",
            "description": "The threat of demonic power has returned to menace the world once again in this action-packed game.",
            "image": "media/game/action4.jfif",
        },
        {
            "name": "Resident Evil Village",
            "description": "Experience survival horror like never before in the 8th major installment in the Resident Evil franchise.",
            "image": "media/game/action5.jfif",
        },
    ],
    "sports_games": [
        {
            "name": "Football Manager 2022",
            "description": "Football isn’t just about being the best and winning. It’s about overcoming the odds, realizing your dreams, and earning your success.",
            "image": "media/game/sport1.jfif",
        },
        {
            "name": "NBA 2K22",
            "description": "NBA 2K22 puts the entire basketball universe in your hands. Play now in real NBA and WNBA environments against authentic teams and players.",
            "image": "media/game/sport2.jfif",
        },
        {
            "name": "EA Sports UFC 4",
            "description": "Shape your legend in the EA SPORTS UFC 4. In EA SPORTS UFC 4 the fighter you become is shaped by your fight style, achievements, and personality.",
            "image": "media/game/sport3.jfif",
        },
        {
            "name": "Tony Hawk's Pro Skater 1 + 2",
            "description": "Drop back in with the most iconic skateboarding games ever made. Play Tony Hawk’s Pro Skater & Tony Hawk’s Pro Skater 2 in one epic collection.",
            "image": "media/game/sport4.jfif",
        },
        {
            "name": "WWE 2K22",
            "description": "Get ripped out of the stands and hit with complete control of the WWE Universe. Throw down with the biggest and most realistic-looking WWE Superstars and Legends.",
            "image": "media/game/sport5.jfif",
        },
    ],
    "strategy_games": [
        {
            "name": "Sid Meier's Civilization VI",
            "description": "Civilization VI offers new ways to interact with your world, expand your empire across the map, advance your culture, and compete against history’s greatest leaders.",
            "image": "media/game/strategy1.jfif",
        },
        {
            "name": "Total War: Three Kingdoms",
            "description": "Three Kingdoms is the first in the award-winning series to recreate epic conflict across ancient China.",
            "image": "media/game/strategy2.jfif",
        },
        {
            "name": "Age of Empires IV",
            "description": "One of the most beloved real-time strategy games returns to glory with Age of Empires IV, putting you at the center of epic historical battles.",
            "image": "media/game/strategy3.jfif",
        },
        {
            "name": "Crusader Kings III",
            "description": "Your legacy awaits. Choose your noble house and lead your dynasty to greatness in a Middle Ages epic that will have you plotting, conquering, and sitting on the throne.",
            "image": "media/game/strategy4.jfif",
        },
        {
            "name": "Stellaris",
            "description": "Explore a vast galaxy full of wonder! Paradox Development Studio brings you the grand strategy game with space exploration at its core.",
            "image": "media/game/strategy5.jfif",
        },
    ],
    "role_play_games": [
        {
            "name": "The Witcher 3: Wild Hunt",
            "description": "As war rages on, you must take on the contract of your life and track down the Child of Prophecy, a key to saving or destroying this world.",
            "image": "media/game/roleplay1.jfif",
        },
        {
            "name": "Divinity: Original Sin 2",
            "description": "The Divine is dead. The Void approaches. And the powers lying dormant within you are soon to awaken. The battle for Divinity has begun.",
            "image": "media/game/roleplay2.jfif",
        },
        {
            "name": "Disco Elysium",
            "description": "Disco Elysium – The Final Cut is the definitive edition of the groundbreaking role-playing game. You’re a detective with a unique skill system at your disposal.",
            "image": "media/game/roleplay3.jfif",
        },
        {
            "name": "Pillars of Eternity II: Deadfire",
            "description": "Pursue a rogue god over land and sea in the sequel to the multi-award-winning RPG Pillars of Eternity. Captain your ship on a dangerous voyage of discovery.",
            "image": "media/game/roleplay4.jfif",
        },
        {
            "name": "GreedFall",
            "description": "Explore uncharted new lands as you set foot on a remote island seeping with magic, and filled with riches, lost secrets, and fantastic creatures.",
            "image": "media/game/roleplay5.jfif",
        },
    ],
    "indie_games": [
        {
            "name": "Hades",
            "description": "Defy the god of the dead as you hack and slash out of the Underworld in this rogue-like dungeon crawler.",
            "image": "media/game/indie1.jfif",
        },
        {
            "name": "Stardew Valley",
            "description": "You’ve inherited your grandfather’s old farm plot in Stardew Valley. Armed with hand-me-down tools and a few coins, you set out to begin your new life.",
            "image": "media/game/indie2.jfif",
        },
        {
            "name": "Celeste",
            "description": "Help Madeline survive her inner demons on her journey to the top of Celeste Mountain, in this super-tight, hand-crafted platformer from the creators of TowerFall.",
            "image": "media/game/indie3.jfif",
        },
        {
            "name": "Undertale",
            "description": "The RPG game where you don’t have to destroy anyone. Each enemy can be “defeated” nonviolently.",
            "image": "media/game/indie4.jfif",
        },
        {
            "name": "Dead Cells",
            "description": "Dead Cells is a rogue-lite, metroidvania inspired, action-platformer. You’ll explore a sprawling, ever-changing castle...",
            "image": "media/game/indie5.jfif",
        },
    ],
}


# Define regex patterns
card_number_regex = re.compile(r"^\d{16}$")
expiry_date_regex = re.compile(r"^(0[1-9]|1[0-2])\/([0-9]{4})$")
cvv_regex = re.compile(r"^\d{3,4}$")


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
    if "username" in session:
        username = session["username"]
        current_user = users.get(username)
        if current_user:
            return render_template("views/account.html", current_user=current_user)
        else:
            flash("User not found.", "error")
            return redirect(url_for("auth.login"))
    else:
        flash("You are not logged in.", "error")
        return redirect(url_for("auth.login"))


@app.route("/top_up_credit", methods=["GET", "POST"])
def top_up_credit():
    if request.method == "POST":
        # Handle form submission and validate payment details
        card_number = request.form.get("card_number", "").strip()
        expiry_date = request.form.get("expiry_date", "").strip()
        cvv = request.form.get("cvv", "").strip()

        # Ensure the inputs are strings (they should be if coming from form)
        if not isinstance(card_number, str):
            flash("Invalid card number format.", "error")
            return render_template("views/top_up_credit.html")
        if not isinstance(expiry_date, str):
            flash("Invalid expiry date format.", "error")
            return render_template("views/top_up_credit.html")
        if not isinstance(cvv, str):
            flash("Invalid CVV format.", "error")
            return render_template("views/top_up_credit.html")

        # Validate card number
        if not card_number_regex.match(card_number):
            flash(
                "Invalid card number. Please enter a valid 16-digit card number.",
                "error",
            )
            return render_template("views/top_up_credit.html")

        # Validate expiry date
        if not expiry_date_regex.match(expiry_date):
            flash(
                "Invalid expiry date. Please enter a valid date in MM/YYYY format.",
                "error",
            )
            return render_template("views/top_up_credit.html")

        # Validate CVV
        if not cvv_regex.match(cvv):
            flash("Invalid CVV. Please enter a valid 3 or 4-digit CVV number.", "error")
            return render_template("views/top_up_credit.html")

        # If all validations pass, top up the user's account
        current_user = users[session["username"]]
        amount = current_user.top_up_option
        current_user.vault_coin += amount
        flash(f"Successfully topped up ${amount} via Credit Card.", "success")
        return redirect(url_for("account"))

    # If it's a GET request, just render the top up credit page
    return render_template("views/top_up_credit.html")


@app.route("/voucher", methods=["GET", "POST"])
def voucher():
    if request.method == "POST":
        voucher_code = request.form.get("voucher-code")
        if (
            voucher_code == "SAMPLEVOUCHER123"
        ):  # Replace with actual voucher validation logic
            current_user = users[session["username"]]
            amount = current_user.top_up_option
            current_user.vault_coin += amount
            flash("Voucher successfully applied!", "success")
            return redirect(url_for("account"))
        else:
            flash("Invalid voucher code. Please try again.", "error")
            return redirect(url_for("top_up"))  # Corrected redirection

    return render_template("views/voucher.html")


@app.route("/update_top_up_option", methods=["POST"])
def update_top_up_option():
    if "username" in session:
        username = session["username"]
        current_user = users.get(username)
        if current_user:
            data = request.get_json()
            amount = int(data["amount"])
            current_user.top_up_option = amount
            return jsonify({"success": True}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Not logged in"}), 401


@app.route("/top_up", methods=["GET", "POST"])
def top_up():
    if request.method == "POST":
        amount_str = request.form.get("amount")
        if amount_str and amount_str.isdigit():
            amount = int(amount_str)
            payment_method = request.form.get("payment")
            current_user = users[session["username"]]

            current_user.top_up_option = amount

            if payment_method == "creditCard":
                return redirect(url_for("top_up_credit"))
            elif payment_method == "voucher":
                return redirect(url_for("voucher"))  # Corrected redirection

            flash("Please select a payment method.", "error")
        else:
            flash("Invalid amount. Please enter a valid number.", "error")

    return render_template("views/top_up.html")


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        payment_method = request.form.get("payment_method")
        if payment_method == "credit_card":
            return redirect(url_for("payment"))
        elif payment_method == "vault_coin":
            return redirect(url_for("vault_payment"))

    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items),
    }
    return render_template(
        "views/checkout.html", cart_summary=cart_summary, cart=cart_items
    )


@app.route("/vault_payment", methods=["GET", "POST"])
def vault_payment():
    current_user = users[session["username"]]
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items),
    }

    if request.method == "POST":
        if current_user.vault_coin >= cart_summary["total_price"]:
            current_user.vault_coin -= cart_summary["total_price"]
            flash(
                f"Payment successful! Remaining Vault Coin balance: {current_user.vault_coin}",
                "success",
            )
            return redirect(url_for("vault_order_summary"))
        else:
            flash(
                "Insufficient Vault Coin balance. Please top up your balance.", "error"
            )
            return redirect(url_for("account"))

    return render_template(
        "views/vault_payment.html",
        cart_summary=cart_summary,
        vault_coin=current_user.vault_coin,
    )


@app.route("/payment", methods=["GET", "POST"])
def payment():
    global payment_details

    if request.method == "POST":
        # Handle form submission and validate payment details
        card_number = request.form.get("card_number", "").strip()
        expiry_date = request.form.get("expiry_date", "").strip()
        cvv = request.form.get("cvv", "").strip()

        # Ensure the inputs are strings (they should be if coming from form)
        if not isinstance(card_number, str):
            flash("Invalid card number format.", "error")
            return render_template(
                "views/payment.html", payment_details=payment_details
            )
        if not isinstance(expiry_date, str):
            flash("Invalid expiry date format.", "error")
            return render_template(
                "views/payment.html", payment_details=payment_details
            )
        if not isinstance(cvv, str):
            flash("Invalid CVV format.", "error")
            return render_template(
                "views/payment.html", payment_details=payment_details
            )

        # Validate card number
        if not card_number_regex.match(card_number):
            flash(
                "Invalid card number. Please enter a valid 16-digit card number.",
                "error",
            )
            return render_template(
                "views/payment.html", payment_details=payment_details
            )

        # Validate expiry date
        if not expiry_date_regex.match(expiry_date):
            flash(
                "Invalid expiry date. Please enter a valid date in MM/YYYY format.",
                "error",
            )
            return render_template(
                "views/payment.html", payment_details=payment_details
            )

        # Validate CVV
        if not cvv_regex.match(cvv):
            flash("Invalid CVV. Please enter a valid 3 or 4-digit CVV number.", "error")
            return render_template(
                "views/payment.html", payment_details=payment_details
            )

        # If all validations pass, update payment details
        payment_details["card_number"] = card_number
        payment_details["expiry_date"] = expiry_date
        payment_details["cvv"] = cvv

        # Dummy payment processing logic
        # For now, let's assume the payment is successful
        # Redirect to order summary page after successful payment
        return redirect(url_for("order_summary"))

    # If it's a GET request, just render the payment page
    return render_template("views/payment.html", payment_details=payment_details)


@app.route("/vault_order_summary")
def vault_order_summary():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items),
    }
    return render_template(
        "views/vault_order_summary.html", cart=cart_items, cart_summary=cart_summary
    )


@app.route("/order_summary")
def order_summary():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items),
    }
    return render_template(
        "views/order_summary.html",
        cart=cart_items,
        cart_summary=cart_summary,
        payment_details=payment_details,
    )


@app.route("/cart")
def cart():
    cart_summary = {
        "total_items": sum(item["quantity"] for item in cart_items),
        "total_price": sum(item["total"] for item in cart_items),
    }
    return render_template(
        "views/cart.html", cart=cart_items, cart_summary=cart_summary
    )


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
        cart_items.append(
            {"name": product_name, "quantity": 1, "price": price, "total": price}
        )
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
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template(
                "views/login.html", message="Invalid credentials. Please try again."
            )

    return render_template("views/login.html")


@app.route("/logout", methods=["POST"])
def logout():
    # Perform logout actions here
    session.pop("username", None)  # Remove the user from the session
    return redirect(url_for("home"))


@app.route("/search")
def search():

    all_games = []
    for category, games in products.items():
        all_games.extend(games)
    
    query = request.args.get("query", "")
    if query:
        results = [
            {
                "id": game.get("id"),
                "name": game.get("name"),
                "description": game.get("description"),
                "image": game.get("image"),
            }
            for game in all_games if query.lower() in game.get("name", "").lower()
        ]
    else:
        results = []
    
    return jsonify(results)