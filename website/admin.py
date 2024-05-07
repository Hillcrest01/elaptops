from flask import Blueprint, render_template, flash, redirect, url_for , send_from_directory
#we are using the send from directory to send the media from the directory for us to be able to view them in the admin page.
from flask_login import login_required, current_user
from .forms import ShopItemForm , OrderForm
from werkzeug.utils import secure_filename
from .models import Product , Customer , Order
from . import db

admin = Blueprint('admin', __name__)

@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media/' , filename)
#currently we are in the admin route, so we need to trace back using .. in orer to get back to the main directory before accessing the media directory.

@admin.route('/add_shop_items', methods=['POST', 'GET'])
@login_required
def add_shop_item():
    if current_user.id != 2:
        return render_template('404.html')

    form = ShopItemForm()
    if form.validate_on_submit():
        product_name = form.product_name.data
        current_price = form.current_price.data
        previous_price = form.previous_price.data
        in_stock = form.in_stock.data
        flash_sales = form.flash_sales.data

        file = form.product_picture.data
        if file and file.filename:
            #ensure you include the file and filename , leaving one leads to attribute error where the application is tryong to access the filename before the file is declared.
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            new_shop_item = Product(
                product_name=product_name,
                current_price=current_price,
                previous_price=previous_price,
                in_stock=in_stock,
                flash_sale=flash_sales,
                product_picture=file_path
            )

            try:
                db.session.add(new_shop_item)
                db.session.commit()
                flash(f'{product_name} added Successfully')
                print('Product Added')
            except Exception as e:
                print("product not added" , e)
                flash('Product Not Added!!')
        else:
            flash('No file uploaded!')

        return redirect(url_for('admin.add_shop_item'))
    return render_template('add_shop_items.html', form=form)

@admin.route('/shop_items' , methods = ['GET' , 'POST'])
@login_required
def shop_items():
    if current_user.id == 2:
        items = Product.query.order_by(Product.date_added).all()
        return render_template('shop_items.html' , items = items)
    else:
        return render_template('404.html')
    

@admin.route('/update_items/<int:item_id>' , methods = ['POST' , 'GET'])
@login_required
def update_items(item_id):
    if current_user.id != 2:
        return render_template('404.html')
    form = ShopItemForm()
    item_to_update = Product.query.get(item_id)

    form.product_name.render_kw = {'placeholder': item_to_update.product_name}
    form.previous_price.render_kw = {'placeholder': item_to_update.previous_price}
    form.current_price.render_kw = {'placeholder': item_to_update.current_price}
    form.in_stock.render_kw = {'placeholder': item_to_update.in_stock}
    form.flash_sales.render_kw = {'placeholder': item_to_update.flash_sale}
    #the render_kw lines above are used to populate data to the fields to be updated with the current data.

    if form.validate_on_submit():
        product_name = form.product_name.data
        current_price = form.current_price.data
        previous_price = form.previous_price.data
        in_stock = form.in_stock.data
        flash_sale = form.flash_sales.data

        file = form.product_picture.data
        if file and file.filename:
            #ensure you include the file and filename , leaving one leads to attribute error where the application is tryong to access the filename before the file is declared.
            file_name = secure_filename(file.filename)
            file_path = f'./media/{file_name}'
            file.save(file_path)

            #this is now the real update in the database, it replaces the old data with the new data.
            try:
                Product.query.filter_by(id=item_id).update(dict(product_name=product_name,
                                                                current_price=current_price,
                                                                previous_price=previous_price,
                                                                in_stock=in_stock,
                                                                flash_sale=flash_sale,
                                                                product_picture=file_path))

                db.session.commit()
                flash(f'{product_name} updated Successfully')
                print('Product Updated')
                return redirect('/shop_items')
            except Exception as e:
                print('Product not Upated', e)
                flash('Item Not Updated!!!')
    return render_template('update_items.html' , form = form)

@admin.route('/delete_items/<int:item_id>' , methods = ['POST' , 'GET'])
@login_required
def delete_items(item_id):
    if current_user.id != 2:
        return render_template('404.html')
    
    try:
        item_to_delete = Product.query.get(item_id)
        db.session.delete(item_to_delete)
        db.session.commit()
        flash('Product deleted successfully')
        return redirect('/shop_items')
    except Exception as e:
        print('item not deleted' , e)
        flash('Product not deleted! , please try again')
    return redirect('/shop_items')

@admin.route('/view_orders')
@login_required
def order_view():
    if current_user.id == 2:
        orders = Order.query.all()
        return render_template('view_orders.html', orders=orders)
    return render_template('404.html')


@admin.route('/update_order/<int:order_id>', methods=['GET', 'POST'])
@login_required
def update_order(order_id):
    if current_user.id == 2:
        form = OrderForm()

        order = Order.query.get(order_id)

        if form.validate_on_submit():
            status = form.order_status.data
            order.order_status = status

            try:
                db.session.commit()
                flash(f'Order {order_id} Updated successfully')
                return redirect('/view_orders')
            except Exception as e:
                print(e)
                flash(f'Order {order_id} not updated')
                return redirect('/view_orders')

        return render_template('order_updates.html', form=form)

    return render_template('404.html')


@admin.route('/customers')
@login_required
def display_customers():
    if current_user.id == 2:
        customers = Customer.query.all()
        return render_template('customers.html', customers=customers)
    return render_template('404.html')


@admin.route('/admin-page')
@login_required
def admin_page():
    if current_user.id == 2:
        return render_template('admin.html')
    return render_template('404.html')