from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    first_name = db.Column(db.String(32), nullable = False)
    last_name = db.Column(db.String(32), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(128), nullable = False)
