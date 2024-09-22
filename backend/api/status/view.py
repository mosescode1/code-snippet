from flask_restx import Namespace, Resource

# Create a Namespace for the status endpoint
stats = Namespace("status", description="Checking api Status")

# Define the resource within the Namespace


@stats.route("", strict_slashes=False)
class StatusApi(Resource):

    def get(self):
        """Returns the status of the api"""
        return {"Status": "online"}
