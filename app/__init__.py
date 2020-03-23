from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///..\db\qu1z.db"
app.config["SECRET_KEY"] = "random key"
db = SQLAlchemy(app)
migrate = Migrate(app, db, directory="db")
from app.models import User

from .views import home_view
from .views import who_view
from .views import hello_view
from .views import users_view


#soap
