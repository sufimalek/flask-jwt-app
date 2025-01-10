import os

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:root@localhost:3316/flask_jwt_app')
    SQLALCHEMY_TRACK_MODIFICATIONS = False