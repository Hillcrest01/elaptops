from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, FloatField , PasswordField ,EmailField , BooleanField , SubmitField , SelectField
from wtforms.validators import DataRequired , Length , NumberRange
from flask_wtf.file import FileField , FileRequired
#filefield and filerequired are used when dealing with images

class SignupForm(FlaskForm):
    email = EmailField('Email' , validators=[DataRequired()])
    username = StringField('username' , validators=[DataRequired() , Length(min=3)])
    password1 = PasswordField('Enter your password' , validators=[DataRequired() , Length(min=6)])
    password2 = PasswordField('Confirm your password' , validators=[DataRequired() , Length(min=6)])
    submit = SubmitField('signup')

class LoginForm(FlaskForm):
    email = EmailField('Enter your email' , validators=[DataRequired()])
    password=PasswordField('Enter your password' , validators=[DataRequired()])
    submit = SubmitField('login')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password' , validators=[DataRequired() , Length(min=6)])
    new_password = PasswordField('New Password' , validators=[DataRequired() , Length(min=6)])
    confirm_new_password = PasswordField('Confirm Password' , validators=[DataRequired() , Length(min=6)])
    change_password = SubmitField('Change Password')

class ShopItemForm(FlaskForm):
    product_name = StringField('Name of Product' , validators=[DataRequired()])
    current_price = FloatField('Current Price' , validators=[DataRequired()])
    previous_price = FloatField('Previous Price' , validators=[DataRequired()])
    in_stock = IntegerField('In Stock' , validators=[DataRequired() , NumberRange(min=0)])
    product_picture =FileField('Product Picture' , validators=[FileRequired()])
    flash_sales = BooleanField('Flash Sales')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update Product')


class OrderForm(FlaskForm):
    order_status = SelectField('Order Status', choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'),
                                                        ('Out for delivery', 'Out for delivery'),
                                                        ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')])

    update = SubmitField('Update Status')