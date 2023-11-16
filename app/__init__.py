from flask import Flask 

from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, Marshmallow
from flask_marshmallow import Marshmallow

from flask_cors import CORS
from helpers import JSONEncoder
#from models import LoginManager
from flask_login import LoginManager


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ayrzdhlj:Np--D33twE3YwEsjuWi0ltc6tcQnfvBL@bubble.db.elephantsql.com/ayrzdhlj'



CORS(app)


migrate = Migrate(app, root_db)
login_manager = LoginManager(app)
ma = Marshmallow(app)

app.register_blueprint(site) #this confirms that everything in 'site' IS our blueprint
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
#db.create_all()
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

