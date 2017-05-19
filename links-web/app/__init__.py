from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from links.context import init_context
from links.logger import get_logger

from settings import SETTINGS

LOGGER = get_logger(__name__)
LOGIN_MANAGER = LoginManager()


def create_app(settings_env):
    init_context()
    app = Flask(__name__)
    app.config.from_object(SETTINGS[settings_env])

    bootstrap = Bootstrap()
    bootstrap.init_app(app)
    LOGIN_MANAGER.init_app(app)
    LOGIN_MANAGER.login_view = 'auth.login'

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
