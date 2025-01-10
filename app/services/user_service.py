from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User

class UserService:
    @staticmethod
    def register_user(username, password, role='user'):
        if User.query.filter_by(username=username).first():
            return None, "Username already exists"

        hashed_password = generate_password_hash(password)
        user = User.create_user(username=username, password=hashed_password, role=role)
        return user, None

    @staticmethod
    def get_all_users():
        return User.get_all_users()

    @staticmethod
    def get_user_by_id(user_id):
        return User.get_user_by_id(user_id)

    @staticmethod
    def update_user(user_id, username=None, role=None):
        return User.update_user(user_id, username, role)

    @staticmethod
    def delete_user(user_id):
        return User.delete_user(user_id)