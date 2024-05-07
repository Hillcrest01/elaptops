from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_database():
    db.create_all()
    print('database created successfully')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yfvryjhfbruifkhnrfnr'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    #we then innitializa our database with the app.
    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return Customer.query.get(int(id))
    #for the purpose of this id, always leave the primary keys of the tables as id and do not tailor make them e.g. customer_id. As get(int(id)) cannot be overriden by another name.
    
    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Cart , Customer , Product


    app.register_blueprint(views , url_prefix = '/')
    app.register_blueprint(admin , url_prefix = '/')
    app.register_blueprint(auth , url_prefix = '/')

     #we call the create_database() function to creat our database

    with app.app_context():
        create_database()

    return app
