from flask import Blueprint, render_template, redirect, url_for, request
from .models import Product
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def home():
    products = Product.query.limit(3).all()  # featured products
    return render_template('index.html', products=products)

@main.route('/shop')
def shop():
    products = Product.query.all()
    return render_template('shop.html', products=products)

@main.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main.route('/checkout/<int:product_id>', methods=['GET', 'POST'])
def checkout(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        bank = request.form.get('bank')
        # Here you would call PayNet FPX API
        # For demo, redirect to success page
        return redirect(url_for('main.success'))
    return render_template('checkout.html', product=product)

@main.route('/success')
def success():
    return render_template('success.html')
