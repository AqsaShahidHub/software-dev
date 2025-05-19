from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
import json
from datetime import datetime
from sqlalchemy import text

from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Import and initialize db after app is created
from models import db, User, Product, Order, OrderItem

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Set the login view
# Don't automatically redirect to login for each page
login_manager.login_message = None  # No message when redirecting

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables and sample data
with app.app_context():
    try:
        # Drop existing tables with cascade
        db.session.execute(text("DROP TABLE IF EXISTS order_item CASCADE"))
        db.session.execute(text("DROP TABLE IF EXISTS \"order\" CASCADE"))
        db.session.execute(text("DROP TABLE IF EXISTS product CASCADE"))
        db.session.execute(text("DROP TABLE IF EXISTS \"user\" CASCADE"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error dropping tables: {e}")
    
    # Create tables
    db.create_all()
    
    # Add sample products if none exist
    if Product.query.count() == 0:
        # Electronics category
        electronics_products = [
            {
                'name': 'Smartphone Pro X',
                'description': 'The latest smartphone with advanced camera features and long battery life.',
                'price': 899.99,
                'image': 'electronics1.jpg',
                'category': 'Electronics'
            },
            {
                'name': 'Ultrabook Slim',
                'description': 'Ultra-thin laptop with powerful performance and 12-hour battery life.',
                'price': 1299.99,
                'image': 'electronics2.jpg',
                'category': 'Electronics'
            },
            {
                'name': 'Wireless Earbuds',
                'description': 'High-quality sound with noise cancellation and comfortable fit.',
                'price': 149.99,
                'image': 'electronics3.jpg',
                'category': 'Electronics'
            },
            {
                'name': 'Smart Watch',
                'description': 'Track your fitness goals and stay connected with this sleek smartwatch.',
                'price': 249.99,
                'image': 'electronics4.jpg',
                'category': 'Electronics'
            },
            {
                'name': '4K Smart TV',
                'description': 'Immersive entertainment experience with vibrant colors and sharp image quality.',
                'price': 799.99,
                'image': 'electronics5.jpg',
                'category': 'Electronics'
            },
            {
                'name': 'Gaming Console',
                'description': 'Next-generation gaming with stunning graphics and exclusive titles.',
                'price': 499.99,
                'image': 'electronics6.jpg',
                'category': 'Electronics'
            }
        ]
        
        # Clothing category
        clothing_products = [
            {
                'name': 'Men\'s Casual Shirt',
                'description': 'Comfortable cotton shirt for everyday wear.',
                'price': 29.99,
                'image': 'clothing1.jpg',
                'category': 'Clothing'
            },
            {
                'name': 'Women\'s Dress',
                'description': 'Elegant dress for special occasions.',
                'price': 59.99,
                'image': 'clothing2.jpg',
                'category': 'Clothing'
            },
            {
                'name': 'Athletic Shoes',
                'description': 'Lightweight and durable shoes for sports and running.',
                'price': 79.99,
                'image': 'clothing3.jpg',
                'category': 'Clothing'
            },
            {
                'name': 'Denim Jeans',
                'description': 'Classic denim jeans with a modern fit.',
                'price': 49.99,
                'image': 'clothing4.jpg',
                'category': 'Clothing'
            },
            {
                'name': 'Winter Jacket',
                'description': 'Warm and waterproof jacket for cold weather.',
                'price': 89.99,
                'image': 'clothing5.jpg',
                'category': 'Clothing'
            },
            {
                'name': 'Summer Hat',
                'description': 'Stylish hat to protect from the sun.',
                'price': 19.99,
                'image': 'clothing6.jpg',
                'category': 'Clothing'
            }
        ]
        
        # Add all products
        all_products = electronics_products + clothing_products
        for product_data in all_products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()

# Home page with categories
@app.route('/')
def index():
    categories = db.session.query(Product.category).distinct().all()
    categories = [c[0] for c in categories]
    
    sample_products = {}
    for category in categories:
        sample_products[category] = Product.query.filter_by(category=category).limit(3).all()
    
    return render_template('index.html', categories=categories, sample_products=sample_products)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Products page filtered by category
@app.route('/products')
@app.route('/products/<category>')
def products(category=None):
    if category:
        products = Product.query.filter_by(category=category).all()
    else:
        products = Product.query.all()
        category = "All Products"
    
    return render_template('products.html', products=products, category=category)

# Product detail page
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_detail.html', product=product)

# Add to cart with stock check
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    product = Product.query.get_or_404(product_id)
    
    # Check if quantity is valid
    if quantity <= 0:
        flash('Please select a valid quantity.', 'danger')
        return redirect(url_for('product_detail', product_id=product_id))
    
    # Check if enough stock
    if quantity > product.stock:
        flash(f'Sorry, only {product.stock} units available.', 'danger')
        return redirect(url_for('product_detail', product_id=product_id))
    
    cart = session.get('cart', {})
    product_id_str = str(product_id)
    
    # Calculate current quantity in cart plus new quantity
    current_qty = cart.get(product_id_str, 0)
    total_qty = current_qty + quantity
    
    # Check if total quantity exceeds stock
    if total_qty > product.stock:
        flash(f'Cannot add {quantity} more. You already have {current_qty} in your cart and only {product.stock} are available.', 'danger')
        return redirect(url_for('product_detail', product_id=product_id))
    
    # Update cart
    if product_id_str in cart:
        cart[product_id_str] += quantity
    else:
        cart[product_id_str] = quantity
    
    session['cart'] = cart
    flash(f'{product.name} added to cart!', 'success')
    return redirect(url_for('cart'))

# Cart page
@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    products = []
    total = 0
    
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            price = product.price * quantity
            total += price
            products.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': price,
                'image': product.image
            })
    
    # Calculate tax and shipping
    tax = total * 0.07  # 7% tax
    shipping = 10.00 if total > 0 else 0  # $10 shipping
    grand_total = total + tax + shipping
    
    return render_template('cart.html', 
                          cart_items=products, 
                          total=total,
                          tax=tax,
                          shipping=shipping,
                          grand_total=grand_total)

# Remove from cart
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        del cart[product_id_str]
        session['cart'] = cart
    
    return redirect(url_for('cart'))


# User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        address = request.form.get('address')
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))
        
        # Check if username or email already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            address=address
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = 'remember' in request.form
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            # Only redirect to next_page if it's a URL within our app
            if next_page and next_page.startswith('/'):
                return redirect(next_page)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
    
    return render_template('login.html')

# User Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# Checkout page
@app.route('/checkout')
@login_required
def checkout():
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('index'))
    
    products = []
    total = 0
    
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            price = product.price * quantity
            total += price
            products.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'quantity': quantity,
                'subtotal': price,
                'image': product.image
            })
    
    # Calculate tax and shipping
    tax = total * 0.07  # 7% tax
    shipping = 10.00  # $10 shipping
    grand_total = total + tax + shipping
    
    return render_template('checkout.html', 
                          cart_items=products, 
                          total=total,
                          tax=tax,
                          shipping=shipping,
                          grand_total=grand_total)

# Process order
@app.route('/process_order', methods=['POST'])
@login_required
def process_order():
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('index'))
    
    # Calculate totals
    total = 0
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            total += product.price * quantity
    
    tax = total * 0.07  # 7% tax
    shipping = 10.00  # $10 shipping
    grand_total = total + tax + shipping
    
    # Create order
    order = Order(
        user_id=current_user.id,
        order_number=Order.generate_order_number(),
        total_amount=total,
        tax_amount=tax,
        shipping_amount=shipping
    )
    db.session.add(order)
    db.session.flush()  # Get the order ID
    
    # Create order items
    for product_id, quantity in cart_items.items():
        product = Product.query.get(int(product_id))
        if product:
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity,
                price=product.price
            )
            db.session.add(order_item)
            
            # Update product stock
            product.stock -= quantity
    
    db.session.commit()
    
    # Clear cart
    session['cart'] = {}
    
    return redirect(url_for('order_confirmation', order_id=order.id))

# Order confirmation
@app.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    if order.user_id != current_user.id:
        flash('Unauthorized access!', 'danger')
        return redirect(url_for('index'))
    
    return render_template('order_confirmation.html', order=order)

@app.route('/order_details/<int:order_id>')
@login_required
def order_details(order_id):
    order = Order.query.get_or_404(order_id)
    
    # Security check - ensure the user only sees their own orders
    if order.user_id != current_user.id:
        flash('You do not have permission to view this order.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Pass current time for checking order age
    now = datetime.utcnow()
    
    return render_template('order_details.html', order=order, now=now)

# User Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    # Get user orders sorted by date (newest first)
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    
    # Calculate accurate total spent
    total_spent = 0
    for order in orders:
        if order.status != 'cancelled':
            total_spent += order.total_amount + order.tax_amount + order.shipping_amount
    
    # Pass current time for checking order age
    now = datetime.utcnow()
    
    return render_template('dashboard.html', orders=orders, total_spent=total_spent, now=now)

# Cancel order
@app.route('/order/<int:order_id>/cancel', methods=['POST'])
@login_required
def cancel_order(order_id):
    order = Order.query.get_or_404(order_id)
    
    # Security check - ensure the user only cancels their own orders
    if order.user_id != current_user.id:
        flash('You do not have permission to cancel this order.', 'danger')
        return redirect(url_for('dashboard'))
    
    # Check order status - allow cancellation for processing and completed (if recent)
    if order.status == 'cancelled':
        flash('This order has already been cancelled.', 'warning')
    elif order.status == 'processing':
        # Cancel the order
        order.status = 'cancelled'
        
        # Restock inventory
        for item in order.items:
            product = item.product
            product.stock += item.quantity
        
        db.session.commit()
        flash('Your order has been cancelled successfully.', 'success')
    elif order.status == 'completed':
        # Check if order is recent (within 24 hours)
        time_difference = datetime.utcnow() - order.order_date
        if time_difference.total_seconds() < 86400:  # 24 hours in seconds
            # Cancel the order
            order.status = 'cancelled'
            
            # Restock inventory
            for item in order.items:
                product = item.product
                product.stock += item.quantity
            
            db.session.commit()
            flash('Your recent order has been cancelled successfully.', 'success')
        else:
            flash('Sorry, completed orders can only be cancelled within 24 hours of purchase.', 'warning')
    elif order.status == 'shipped':
        flash('Sorry, shipped orders cannot be cancelled. Please contact customer support.', 'warning')
    else:
        flash('This order cannot be cancelled.', 'warning')
    
    # Get the referer to determine where to redirect back to
    referer = request.headers.get('Referer')
    if referer and 'dashboard' in referer:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('order_details', order_id=order.id))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)