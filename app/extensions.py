from flask import request
from flask_wtf import CSRFProtect 
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap5
from flask_cors import CORS 

bcrypt = Bcrypt()
bootstrap = Bootstrap5()
cors = CORS()
csrf = CSRFProtect()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
migrate = Migrate()


def register_extensions(app):
    """
    """
    bcrypt.init_app(app)
    bootstrap.init_app(app)
    cors.init_app(app, resources={
        r"/client/*": {
            "origins": "*"
        }
    })
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
