from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

from .views import home_view
from .views import who_view
from .views import hello_view


#soap


