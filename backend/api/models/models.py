from api import db, bycrypt
from .Base_model.base_model import BaseModel
from datetime import datetime


class User(db.Model, BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), unique=True, nullable=False)
    bio = db.Column(db.String(120), default="Programmer")
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationship
    snippets = db.relationship('Snippet', backref="users", lazy=True)

    def __init__(self, firstname, lastname, username, email, bio=None) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.bio = bio

    def __repr__(self) -> str:
        return f"User({self.username})"

    def hash_password(self, password):
        hd_pwd = bycrypt.generate_password_hash(password)
        self.password = hd_pwd

    def check_passsord(self, passsord):
        return bycrypt.check_password_hash(self.password, passsord)


class Snippet(db.Model, BaseModel):
    __tablename__ = "snippets"

    id = db.Column(db.Integer, primary_key=True)
    snippet_type = db.Column(db.String(100), nullable=False)
    snippet_code = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, snippet_type, snippet_code, user_id) -> None:
        self.snippet_type = snippet_type
        self.snippet_code = snippet_code
        self.user_id = user_id

    def __repr__(self) -> str:
        return f"Snippets({self.snippet_type}) User({self.user_id})"
