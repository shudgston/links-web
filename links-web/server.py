import os
from app import create_app

# TODO -- remove this code; testing only
APP = create_app(os.environ.get('FLASK_SETTINGS_ENV', 'default'))
APP.run(host=APP.config['BIND'])
