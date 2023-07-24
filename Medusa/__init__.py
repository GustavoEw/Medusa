from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "1234"
database = SQLAlchemy(app)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
from Medusa import routes
