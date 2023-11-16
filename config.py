#config allows our app to talk to whatever it is running on. (cloud, and other devices)
import os #os is a module that lets the app talk to a computer

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, 'env'))


class Config():
    '''
    Set config to variables for the flask app
    using enviornment variables where available.
    Otherwise, create the config variable if not done already.
    '''
    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I dont know what I am doing here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False