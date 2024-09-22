from flask_restx import Namespace, Resource, fields, reqparse
# import requests
parser = reqparse.RequestParser()
parser.add_argument('page')
parser.add_argument('limit')
# args = parser.parse_args()


snippets = Namespace("snippets", description="Snippets route")


get_snippet_model = snippets.model("Return all snippets", {
    "id": fields.Integer,
    "snippet_type": fields.String,
    "snippet_code": fields.String,
    "user_id": fields.Integer,
    # "user": fields.String(
    #     attribute=lambda x: f"http://localhost:5000/users/{x['user_id']}"),
    # "snippet_url": fields.String(
    #     attribute=lambda x: f"http://localhost:5000/users/{x['user_id']}/snippets/{x['id']}")
})


@snippets.route("")
class snippetsRoute(Resource):

    @snippets.marshal_with(get_snippet_model)
    def get(self):
        """Returns all snippets in the database"""
        from api.models.models import Snippet

        args = parser.parse_args()
        if args["limit"] is not None or args["page"] is None:
            args["page"] = 1
            args["limit"] = 7

        return [snippet.to_json() for snippet in Snippet.query.paginate(page=int(args["page"]), max_per_page=int(args["limit"]))]


@snippets.route("/<int:id>")
@snippets.doc(params={'id': 'An ID'})
class singleSnippet(Resource):

    @snippets.marshal_with(get_snippet_model)
    def get(self, id):
        """gets a single snippets"""
        from api.models.models import Snippet
        snippet = Snippet.query.get(id)

        if not snippet:
            return {'status': 'Not Found'}, 404

        return snippet.to_json(), 200
