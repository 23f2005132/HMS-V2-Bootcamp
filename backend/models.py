from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    toppings = db.Column(db.String(200), nullable=True)