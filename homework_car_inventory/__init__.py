from flask import Flask
from config import Config

from .main_site.routes import main_site
from .authentication.routes import auth
from .api.routes import api

from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma

from flask_cors import CORS #Importing this, assuming our future homework will also implement CORS

from .helpers import JSONEncoder

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_site)
app.register_blueprint(auth)
app.register_blueprint(api)
#creating basic routes 

#this essentially allows us to connect SQLAlchemy and Flask together
root_db.init_app(app)
migrate = Migrate(app, root_db)

login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

CORS(app)

app.json_encoder = JSONEncoder

from homework_car_inventory import models