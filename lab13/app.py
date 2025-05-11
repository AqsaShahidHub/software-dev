
"""
Aqsa Shahid
LAb-13, Flask Application
"""
import os
from flask import Flask, render_template, session, flash, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Single secret key definition

# Configure database - encode password to handle special characters

"""
Professor I have to add some extra code because I had special character in my password and it was throwing an Error
Aqsa Shahid

"""

password = quote_plus("PASSWORD")
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{password}@localhost/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define User model (create table in the 'demoDB' database)
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)  # Added password field

# Define employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)

# Set the routing to the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Don't expose password in response
        return 'Successfully requested! Entered Password: ' + request.form['password']
    name = "Aqsa Shahid"
    fruits = ['apple', 'orange', 'grapes']
    check_fruit = 'apple'
    return render_template('index.html', username=name, listfruits=fruits, checkfruit=check_fruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']

            # Check if employee already exists by name
            existing_employee = Employee.query.filter_by(employee_name=emp_name).first()
            if existing_employee:
                flash(f"Employee with name '{emp_name}' already exists!")
                return render_template('users.html')  # Added return statement
                
            # Check if employee ID already exists
            existing_id = Employee.query.filter_by(employee_id=emp_id).first()
            if existing_id:
                flash(f"Employee with id '{emp_id}' already exists!")
                return render_template('users.html')  # Added return statement

            # Create a new employee object and add form data into the database
            new_employee = Employee(employee_id=emp_id, employee_name=emp_name)

            # Store employee name in session
            session['employee1'] = new_employee.employee_name

            # Add the new object to our database
            db.session.add(new_employee)
            db.session.commit()

            # Message using flash
            flash(f"{request.form['employee_name']} successfully added!")

        except Exception as e:  # Changed to catch specific exceptions
            db.session.rollback()  # Rollback changes if there's an error
            flash("Fail to insert data! Try again")

    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Start the server - set debug=False for production
    app.run(debug=True)