from flask_restx import Namespace, Resource, fields
from flask_restx import reqparse
from utils import validate_user

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate to charge for this resource')


# Create a Namespace for the status endpoint
users = Namespace("users", description="Returns all Users")

# Define the resource within the Namespace
get_model = users.model('Get users', {
    "id": fields.Integer(required=True),
    'firstname': fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "email": fields.String,
    "bio": fields.String,
    "joined_at": fields.String,
    # Ensure this matches the Namespace endpoint
    'url': fields.Url(endpoint="user_detail", absolute=True)
})

post_model = users.model("Create User", {
    'firstname': fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "email": fields.String,
})


@users.route("/", strict_slashes=False, endpoint="get")
class Users(Resource):

    @users.expect(post_model, validate=True)
    @users.doc(responses={201: "user Created"})
    def post(self):
        from api.models.models import User

        user_details = users.payload
        if not validate_user(user_details):
            return {"Status": "some Data missing"}

        user = User(**user_details)
        user.save()

        return {"status": "Created Successfully"}, 201

    @users.marshal_with(get_model)
    def get(self):
        from api.models.models import User

        # Return a dictionary directly; Flask-RESTx will handle the conversion to JSON
        users = User.query.all()

        return [user.to_json() for user in users], 200


@users.route("/<int:id>", endpoint="user_detail")
class UserDetailResource(Resource):

    @users.marshal_with(get_model)
    def get(self, id):
        from api.models.models import User

        # Retrieve the user by ID
        user = User.query.get_or_404(id)

        # Return the user dictionary
        return user.to_json(), 200

    @users.expect(post_model)
    def put(self, id):
        from api.models.models import User
        users_data = User.query.get_or_404(id)
        payload = users.payload

        for k, v in payload.items():
            if hasattr(users_data, k):
                setattr(users_data, k, v)

        users_data.update()
        print(payload)
        return {"message": "User updated successfully"}, 200

    def delete(self, id):
        from api.models.models import User

        users = User.query.get_or_404(id)

        users.delete()

        return {"status": "Deleted successfull"}, 200
