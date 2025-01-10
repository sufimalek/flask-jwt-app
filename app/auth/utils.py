from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User

def create_user(username, password, role='user'):
    hashed_password = generate_password_hash(password)
    print(f"Hashed password: {hashed_password}")  # Debugging
    user = User(username=username, password=hashed_password, role=role)
    return user

def verify_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        print(f"Stored hash: {user.password}")  # Debugging
        print(f"Password match: {check_password_hash(user.password, password)}")  # Debugging
    if user and check_password_hash(user.password, password):
        return user
    return None