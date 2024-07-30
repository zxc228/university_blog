from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()


login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'danger'

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('main/settings.py')
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from blog.main.routes import main
    from blog.user.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)
    
    @login_manager.user_loader
    def load_user(user_id):
        from blog.models import User
        return User.query.get(int(user_id))
    return app

# app_ctx = create_app()

# def create_user():
#     with app_ctx.app_context():
#         from blog.models import User

#         db.drop_all()
#         db.create_all()

#         hashed_password = bcrypt.generate_password_hash('123456').decode('utf-8')
#         user = User(username='Ilya', email='ilya@gblog.com', password=hashed_password)
#         db.session.add(user)
#         db.session.commit()

