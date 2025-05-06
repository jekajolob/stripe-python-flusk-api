from flask import Flask, request, jsonify, render_template
import stripe
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_url_path="", static_folder="static", template_folder="templates")

# Replace with your test key
stripe.api_key = os.getenv("API_SECRET_KEY")

# Add error handling if API key is not set
if not stripe.api_key:
    raise ValueError("No API key found. Make sure API_SECRET_KEY is set in your environment variables.")

YOUR_DOMAIN = "http://localhost:4242"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Magic Wand 🪄",
                        },
                        "unit_amount": 1500,  # $15.00
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=YOUR_DOMAIN + "/success",
            cancel_url=YOUR_DOMAIN + "/cancel",
        )
        return jsonify({"url": checkout_session.url})
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(port=4242)
