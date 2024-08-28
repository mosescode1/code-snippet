from api import db
from Base_model import BaseModel
from datetime import datetime


class User(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    bio = db.Column(db.String(120), default="Alx learner")
    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(60), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    snippet = db.Column(db.String())
