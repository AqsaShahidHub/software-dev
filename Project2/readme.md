# TechTreasures - E-Commerce Website (Full-Stack Project)

TechTreasures is a fully functional **e-commerce web application** built with Flask and Bootstrap, providing a comprehensive online shopping experience. The application features product browsing by category, detailed product pages, shopping cart management, user authentication, order processing, and a user dashboard for tracking order history.

---

##  Project Structure 

techtreasures/
├── app.py # Application entry point and route definitions
├── config.py # Configuration settings
├── models.py # Database models and relationships
├── requirements.txt # Project dependencies
├── static/ # Static assets
│ ├── css/ # CSS stylesheets
│ │ └── style.css # Custom styles
│ └── images/ # Product and site images
└── templates/ # HTML templates
├── about.html # About page
├── base.html # Base template with common elements
├── cart.html # Shopping cart
├── checkout.html # Checkout process
├── dashboard.html # User dashboard
├── index.html # Homepage
├── login.html # User login
├── order_*.html # Order-related templates
├── product_detail.html # Individual product view
├── products.html # Product listing
└── register.html # User registration
└── screenshots/ # website screenshot images
  └── cart.jpg
  └── home.jpg
  └── checkout.jpg
  └── dashboard.jpg
  └── products.jpg
  └── products_details.jpg
  └── register.jpg
  └── order_confirmation.jpg
└── readme.md

- **Front-End**:
  - HTML/CSS
  - Bootstrap 5
  - JavaScript
- **Back-End**:
  - Python
  - Flask
    - Flask-SQLAlchemy
    - Flask-Login
    - Flask-WTF
  - SQLAlchemy
- **Database**:
  - PostgreSQL
- **Other Tools**:
  - Bootstrap Icons
  - VS Code

---

## 💡 Features

### 🏠 Home Page
- Dynamic hero section with animated elements
- Featured product categories
- "Why Choose Us" section highlighting key benefits

### 🛍️ Product Catalog
- **Two main categories**: Electronics and Clothing
- Each category features multiple products
- Product cards display:
  - Name
  - Image
  - Brief description
  - Price
  - Category badge
  - Quick "Add to Cart" button

### 📱 Product Detail Pages
- Comprehensive product information
- High-quality product images
- Detailed specifications and features
- Customer reviews
- Quantity selection
- "Add to Cart" functionality
- Social sharing options

### 🛒 Shopping Cart
- Real-time cart management
- Quantity adjustments
- Item removal
- Price calculations with tax and shipping
- Checkout options for registered users

### 👤 User Authentication
- User registration form collecting:
  - First and Last Name
  - Username
  - Email
  - Password (securely hashed)
  - Shipping Address
- Login system with session management
- Duplicate username/email validation

### 📋 User Dashboard
- Order history with detailed view
- Account information
- Total spending summary
- Order cancellation for recent orders

### ✅ Checkout & Order Processing
- Streamlined checkout process
- Order summary with line items and totals
- Order confirmation with unique order number
- Status tracking for all orders

### 📑 About Page
- Company information and history
- Team member profiles
- Contact information and form

---

## 🗃️ Database Schema

### `user` Table
| Field        | Type        | Notes                              |
|--------------|-------------|------------------------------------|
| id           | Integer     | Primary key, auto-incrementing     |
| first_name   | String(50)  | User's first name                  |
| last_name    | String(50)  | User's last name                   |
| username     | String(50)  | Unique username                    |
| email        | String(120) | Unique email address               |
| password_hash| String(256) | Securely hashed password           |
| address      | String(200) | Shipping address                   |
| created_at   | DateTime    | Account creation timestamp         |

### `product` Table
| Field       | Type        | Notes                           |
|-------------|-------------|----------------------------------|
| id          | Integer     | Primary key, auto-incrementing   |
| name        | String(100) | Product name                     |
| description | Text        | Detailed product description     |
| price       | Float       | Product price                    |
| image       | String(100) | Image filename                   |
| category    | String(50)  | Product category                 |
| stock       | Integer     | Available inventory (default: 10)|
| created_at  | DateTime    | Product creation timestamp       |

### `order` Table
| Field          | Type        | Notes                           |
|----------------|-------------|----------------------------------|
| id             | Integer     | Primary key, auto-incrementing   |
| user_id        | Integer     | Foreign key to user.id           |
| order_number   | String(20)  | Unique order identifier          |
| total_amount   | Float       | Subtotal before tax & shipping   |
| tax_amount     | Float       | Tax amount                       |
| shipping_amount| Float       | Shipping cost                    |
| order_date     | DateTime    | Order creation timestamp         |
| status         | String(20)  | Order status (completed/cancelled)|

### `order_item` Table
| Field      | Type      | Notes                         |
|------------|-----------|-------------------------------|
| id         | Integer   | Primary key, auto-incrementing|
| order_id   | Integer   | Foreign key to order.id       |
| product_id | Integer   | Foreign key to product.id     |
| quantity   | Integer   | Number of items ordered       |
| price      | Float     | Unit price at time of order   |

---
## Key Relationships

User to Orders: One-to-Many (one user can have multiple orders)
Order to Order Items: One-to-Many (one order can contain multiple items)
Product to Order Items: One-to-Many (one product can be in multiple order items)

## 🎯 Project Goals

This project was developed to create a modern, responsive e-commerce platform that demonstrates:

- Full-stack development capabilities
- User authentication and session management
- Database design and integration
- Shopping cart implementation
- Order processing workflow
- Responsive design principles

The application showcases how to build a complete e-commerce system with Flask, combining both aesthetic design and functional back-end logic.

---

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.jpg)

### Product Catalog
![Product Catalog](screenshots/products.jpg)

### Product Detail
![Product Detail](screenshots/product_detail.jpg)

### Shopping Cart
![Shopping Cart](screenshots/cart.jpg)

### Checkout Page
![Checkout](screenshots/checkout.jpg)

### Order Confirmation
![Order Confirmation](screenshots/order_confirmation.jpg)

### User Dashboard
![Dashboard](screenshots/dashboard.jpg)

### User Registration
![Registration](screenshots/register.jpg)

---

## 🚀 Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/techtreasures.git
   cd techtreasures
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Update PostgreSQL connection in config.py:
   ```python
   # Update with your database details
   password = quote_plus('your_password')
   SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{password}@localhost:5432/techtreasures'
   ```

5. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```
   python app.py
   ```

7. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

---

## 🔄 Future Enhancements

- User profile editing
- Admin panel for product and order management
- Wishlist functionality
- Product reviews and ratings
- Payment gateway integration
- Email notifications
- Advanced search and filtering
- Related products suggestions

---

## 🙏 Acknowledgments

- Special Thanks to Professor Hui Wu, whose guidance and encouragement were invaluable throughout the completion of this project. 

---
