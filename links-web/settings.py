import os


class Settings:
    BIND = '127.0.0.1'
    DEBUG = False
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')


class DevSettings(Settings):
    DEBUG = True


class ProdSettings(Settings):
    BIND = '0.0.0.0'


# Use env var FLASK_SETTINGS_ENV
SETTINGS = {
    'default': DevSettings,
    'dev': DevSettings,
    'prod': ProdSettings,
}
