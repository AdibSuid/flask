from flask import render_template, request, redirect, url_for, session
from app import app

# Mock products for demo
PRODUCTS = [
    {"id": 1, "name": "Smartphone X", "price": 999, "image": "/static/images/product1.jpg"},
    {"id": 2, "name": "Wireless Headphones", "price": 199, "image": "/static/images/product2.jpg"},
    {"id": 3, "name": "Smartwatch Pro", "price": 299, "image": "/static/images/product3.jpg"}
]

# Homepage
@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Shop page
@app.route("/shop")
def shop():
    return render_template("shop.html", products=PRODUCTS)

# Product detail
@app.route("/product/<int:product_id>")
def product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template("product.html", product=product)

# Cart functionality
@app.route("/cart")
def cart():
    if "cart" not in session:
        session["cart"] = []
    cart_items = [p for p in PRODUCTS if p["id"] in session["cart"]]
    total = sum(item["price"] for item in cart_items)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(product_id)
    session.modified = True
    return redirect(url_for("cart"))

@app.route("/checkout")
def checkout():
    # Example integration: Stripe API (mock)
    # Normally you would call Stripe checkout API here
    return "Redirecting to payment gateway..."
