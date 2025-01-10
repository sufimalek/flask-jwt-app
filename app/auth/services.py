from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from app.models.user import User

class AuthService:
    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return None, "Invalid credentials"

        access_token = create_access_token(identity=username)
        return access_token, None