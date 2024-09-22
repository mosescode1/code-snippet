from flask_restx import Namespace, Resource, fields, reqparse
from utils import validate_user
import datetime

parser = reqparse.RequestParser()
parser.add_argument('page')
parser.add_argument('limit')
# args = parser.parse_args()


# Create a Namespace for the status endpoint
users = Namespace("users", description="User Operations")

# Define models
get_model = users.model('Get users', {
    "id": fields.Integer(required=True, default=1),
    'firstname': fields.String(default='John'),
    "lastname": fields.String(default='Doe'),
    "username": fields.String(default='johndoe'),
    "email": fields.String(default='john.doe@example.com'),
    "bio": fields.String(default="This is my bio"),
    "joined_at": fields.String(default=datetime.datetime.utcnow().isoformat()),
    'url': fields.Url(endpoint="user_detail", absolute=True, default=f"/users/1"),
})

post_model = users.model("Create User", {
    'firstname': fields.String(default='John'),
    "lastname": fields.String(default='Doe'),
    "username": fields.String(default='johndoe'),
    "email": fields.String(default='john.doe@example.com'),
    "password": fields.String(default='password123'),
})

get_snippet_model = users.model("Return all snippets", {
    "id": fields.Integer,
    "snippet_type": fields.String,
    "snippet_code": fields.String,
    "user_id": fields.Integer,
    # "user": fields.String(
    #     attribute=lambda x: f"http://localhost:5000/users/{x['user_id']}"),
    # "snippet_url": fields.String(
    #     attribute=lambda x: f"http://localhost:5000/users/{x['user_id']}/snippets/{x['id']}")
})

snippet_model = users.model("Create snippet", {
    "snippet_type": fields.String(default='Javascript'),
    "snippet_code": fields.String(default="console.log(`hello world`)"),
})


@users.route("", strict_slashes=False, endpoint="getAll")
class Users(Resource):

    @users.expect(post_model, validate=True)
    @users.doc(responses={201: "User Created"})
    def post(self):
        """Creates a new user in the database"""
        from api.models.models import User

        user_details = users.payload
        if not validate_user(user_details):
            return {"status": "Some data missing"}, 400

        password = user_details.pop('password')
        user = User(**user_details)
        user.hash_password(password=password)
        user.save()

        return {"status": "Created Successfully"}, 201

    @users.marshal_with(get_model)
    def get(self):
        """Returns all users in the database"""
        from api.models.models import User
        args = parser.parse_args()

        # ! pagination
        # if args["limit"] is not None or args["page"] is None:
        #     args["page"] = 1
        #     args["limit"] = 2

        users = User.query.paginate(args["page"], args["limit"])
        return [user.to_json() for user in users], 200


@users.route("/<int:id>", endpoint="user_detail")
class UserDetailResource(Resource):

    @users.marshal_with(get_model)
    @users.doc(params={'id': 'An ID'})
    def get(self, id):
        """Get a single user from the database"""
        from api.models.models import User
        user = User.query.get_or_404(id)
        return user.to_json(), 200

    @users.expect(post_model)
    def patch(self, id):
        """Update a user profile"""
        from api.models.models import User
        users_data = User.query.get_or_404(id)
        payload = users.payload

        for k, v in payload.items():
            if hasattr(users_data, k):
                setattr(users_data, k, v)

        users_data.update()
        return {"status": "User updated successfully"}, 200

    @users.doc(responses={200: "Deleted Successfull"})
    def delete(self, id):
        """Delete a user"""
        from api.models.models import User
        user = User.query.get_or_404(id)
        user.delete()
        return {"status": "Deleted successfully"}, 200


@users.route("/<int:id>/snippets", endpoint="user_snippet")
class usersnippetResource(Resource):

    @users.marshal_with(get_snippet_model)
    def get(self, id):
        from api.models.models import User

        user = User.query.get(id)
        if not user:
            return {"status": "Bad Request"}, 404

        return [snippet.to_json() for snippet in user.snippets], 200

    @users.expect(snippet_model)
    def post(self, id):
        from api.models.models import User, Snippet
        user = User.query.get(id)
        if not user:
            return {"status": "Bad Request"}, 404

        data = users.payload
        if not data:
            return {"status": "Missing Information"}, 400

        snippet = Snippet(snippet_type=data["snippet_type"],
                          snippet_code=data["snippet_code"], user_id=user.id)
        snippet.save()

        return {"status": "Created Successfully"}, 201
