from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from webconfig import Config

flask_website = Flask(__name__)
flask_website.config.from_object(Config)
db = SQLAlchemy(flask_website)
migrate = Migrate(flask_website, db)
login = LoginManager(flask_website)
login.login_view = 'login'

from flask_website import routes, models