from api import code_app, db
# from backend.api.models.models import User
from api.models.models import User


if __name__ == "__main__":
    with code_app.app_context():
        db.drop_all()
        db.create_all()
        user = User("Effass", "emmanuelss", "ossigma11ss",
                    email="iammosess20@gmail.com")
        user.save()
    code_app.run(debug=True)
