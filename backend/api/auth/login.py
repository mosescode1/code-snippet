from flask_restx import Resource, Namespace, fields


login = Namespace("auth", description="Login route")

login_model = login.model("login", {
    "username": fields.String(default='ossigma123'),
    "password": fields.String(default="12345"),
})


@login.route("/login")
class loginRoute(Resource):
    @login.expect(login_model)
    def post(self):
        """Authenticate user"""
        from api.models.models import User

        data = login.payload
        if not data:
            return {"error": "Missing Informaion"}, 400

        if (data['username'] is None or data['password'] is None):
            return {"error": "Missing Informaion"}, 400

        user = User.query.filter_by(username=data['username']).first()

        if not user:
            return {
                "status": "fail",
                "statusCode": 404,
                "error": "User Not Found"
            }, 404

        if not user.check_passsord(data['password']):
            return {
                "status": "fail",
                "statusCode": 404,
                "error": "Wrong password"
            }, 404

        return {
            "status": "OK",
            "statusCode": 200,
            "data": user.to_json()
        }, 202
