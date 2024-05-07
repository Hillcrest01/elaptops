from flask import Blueprint , request , flash , redirect , url_for , render_template
from .models import Customer
from . import db
from .forms import SignupForm , LoginForm , PasswordChangeForm
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user , current_user , logout_user , login_required , LoginManager

auth = Blueprint('auth' , __name__)

@auth.route('/signup' , methods = ['POST' , 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
       email = request.form.get('email')
       username = request.form.get('username')
       password1 = request.form.get('password1')
       password2 = request.form.get('password2')

       new_customer = Customer.query.filter_by(email = email).first()
       if new_customer:
           flash('email already registered , please try a new email')
       elif password1 == password2:
           new_customer = Customer(email = email , username = username , password_hash = generate_password_hash(password1))
           db.session.add(new_customer)
           db.session.commit()
           flash('Account created successfully , you can now log in ')
           login_user(new_customer , remember=True)

           return redirect(url_for('auth.login'))
       else:
           flash('passwords do not match')

    return render_template('signup.html' , form = form , new_customer = current_user)
    
    #since SignupForm is a class, ensure you include the brackets when calling it.

@auth.route('/login' , methods = ['POST' , 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = request.form.get('email')
        password = request.form.get('password')
        
        new_customer = Customer.query.filter_by(email = email).first()

        if new_customer:
            if check_password_hash(new_customer.password_hash , password):
                #password hash is the name of the passwords table in the database, password is what the user has entered, so it checks the two if they are matching.
                flash('login successful')
                login_user(new_customer , remember = True)
                return redirect('/')
            
            else:
                flash('incorrect password or email')
        
        else:
            flash('There is no account linked with this email , sign up to continue')
            return redirect(url_for('auth.signup'))
        
    return render_template('login.html' , form = form , new_customer = current_user)

@auth.route('/logout' , methods = ['POST' , 'GET'])
@login_required
def logout():
    logout_user()
    flash('you have been successfully logged out')
    return redirect('/')

@auth.route('/profile/<int:customer_id>' , methods = ['POST' , 'GET'])
def profile(customer_id):
    customer = Customer.query.get(customer_id)
    return render_template('profile.html' , customer = customer)

@auth.route('/changepassword/<int:customer_id>' , methods = ['POST' , 'GET'])
#do not include any spaces between int and customer_id. It breaks the url_prefix rule
@login_required
def change_password(customer_id):
    form = PasswordChangeForm()
    customer = Customer.query.get(customer_id)

    #make sure you add the parenthesis as without them nothing is passed from the backend to the frontend.
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if customer.verify_password(current_password):
            if new_password == confirm_new_password:
                customer.password = confirm_new_password
                db.session.commit()
                flash('Password Updated Successfully')
                return redirect(f'/profile/{customer.id}')
            else:
                flash('New Passwords do not match!!')

        else:
            flash('Current Password is Incorrect')

    return render_template('change_password.html', form=form)