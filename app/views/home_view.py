from app import app


@app.route("/")
def home():
	return "Please go to an actual address."