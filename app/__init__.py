from flask import Flask

from .extensions import register_extensions
from .config import config_options
from .template_filters import register_jinja_filters



def register_blueprints(app):
    """
    """
    from .auth import blueprint as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from .client import blueprint as client_bp
    app.register_blueprint(client_bp, url_prefix='/client')

    from .employee import blueprint as employee_bp
    app.register_blueprint(employee_bp, url_prefix='/employee')

    from .main import blueprint as main_bp
    app.register_blueprint(main_bp)

    from .spa import blueprint as spa_bp
    app.register_blueprint(spa_bp, url_prefix='/spa')


def create_app(config_name):
    """
    """
    app = Flask(__name__, static_folder='./static', template_folder='./templates')
    app.config.from_object(config_options[config_name])
    

    register_extensions(app)
    register_blueprints(app)
    register_jinja_filters(app)


    return app
