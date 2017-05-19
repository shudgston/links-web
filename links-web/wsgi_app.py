import os
from app import create_app

APP = create_app(os.environ.get('FLASK_SETTINGS_ENV', 'default'))
