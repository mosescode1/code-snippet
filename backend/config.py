import os

""" 
ALXCONNECT CONFIGURATION FILE
"""


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "code_snipper"
    SQLALCHEMY_DATABASE_URI = "sqlite:///codesnipe.db"
