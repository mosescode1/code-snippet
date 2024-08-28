from flask_restx import Namespace, Resource, fields, reqparse
from utils import validate_user

# Create a Namespace for the status endpoint
users = Namespace("users", description="User Operations")

# Define models
get_model = users.model('Get users', {
    "id": fields.Integer(required=True),
    'firstname': fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "email": fields.String,
    "bio": fields.String,
    "joined_at": fields.String,
    'url': fields.Url(endpoint="user_detail", absolute=True),
    "user_snippets": fields.Url(endpoint="user_snippet", absolute=True)
})

post_model = users.model("Create User", {
    'firstname': fields.String,
    "lastname": fields.String,
    "username": fields.String,
    "email": fields.String,
})

snippet_model = users.model("Create snippet", {
    "id": fields.Integer,
    "user_id": fields.Integer,
    "snippet_type": fields.String,
    "snippet_code": fields.String,
})


get_snippet_model = users.model("Return all snippets", {
    "id": fields.Integer,
    "snippet_type": fields.String,
    "snippet_code": fields.String,
    "user_id": fields.Integer,
    "user": fields.String(
        attribute=lambda x: f"http://localhost:5000/users/{x['user_id']}")
})


@users.route("/", strict_slashes=False, endpoint="get")
class Users(Resource):

    @users.expect(post_model, validate=True)
    @users.doc(responses={201: "User Created"})
    def post(self):
        from api.models.models import User

        user_details = users.payload
        if not validate_user(user_details):
            return {"status": "Some data missing"}, 400

        user = User(**user_details)
        user.save()

        return {"status": "Created Successfully"}, 201

    @users.marshal_with(get_model)
    def get(self):
        from api.models.models import User
        users = User.query.all()
        return [user.to_json() for user in users], 200


@users.route("/<int:id>", endpoint="user_detail")
class UserDetailResource(Resource):

    @users.marshal_with(get_model)
    def get(self, id):
        from api.models.models import User
        user = User.query.get_or_404(id)
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
        return {"status": "User updated successfully"}, 200

    def delete(self, id):
        from api.models.models import User
        user = User.query.get_or_404(id)
        user.delete()
        return {"status": "Deleted successfully"}, 200


@users.route("/<int:id>/snippets", endpoint="user_snippet")
class UserSnippetResource(Resource):

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

        print(data)

        snippet = Snippet(snippet_type=data["snippet_type"],
                          snippet_code=data["snippet_code"], user_id=user.id)
        snippet.save()

        return {"status": "Created Successfully"}, 201
