from flask import Flask


app = Flask(__name__)

from .views import home_view
from .views import who_view
from .views import hello_view


