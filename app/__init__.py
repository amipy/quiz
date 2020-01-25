from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
	return "Hello"
	
@app.route("/who")
def who():
	return "Alex did"
	
@app.route("/")
def home():
	return "Please go to an actual address."