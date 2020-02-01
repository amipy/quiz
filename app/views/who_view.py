from app import app

@app.route("/who")
def who():
    return "Alex did"