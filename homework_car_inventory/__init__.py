from flask import Flask
from config import Config

from .main_site.routes import main_site
from .authentication.routes import auth

from flask_migrate import Migrate
from .models import db as root_db

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(main_site)
app.register_blueprint(auth)
#creating basic routes 

#this essentially allows us to connect SQLAlchemy and Flask together
root_db.init_app(app)
migrate = Migrate(app, root_db)

from homework_car_inventory import models