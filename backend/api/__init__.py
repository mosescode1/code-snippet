from flask import Blueprint, Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_cors import CORS
from config import Config
from flask_bcrypt import BCrypt

# !routes
from .status.view import stats
from .users.view import users
# Initialize Flask app
code_app = Flask(__name__)

# Setup CORS
cors = CORS(code_app, resources={r"/api/v1*": {"origins": "*"}})

# Load configuration
code_app.config.from_object(Config)

bycrypt = BCrypt(code_app)

# Setup SQLAlchemy with a custom declarative base


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(code_app)

# Create a Flask Blueprint
blueprint = Blueprint('CodeSnipper', __name__, url_prefix='/api/v1')

# Initialize Api with the Blueprint
api = Api(code_app, title="CodeSnipper",
          default_swagger_filename="codeSnipper")

# Add namespaces to the Api
api.add_namespace(stats)
api.add_namespace(users)

# # Register the Blueprint with the Flask app
code_app.register_blueprint(blueprint)
