import pytest
from app import create_app
from app.models.user import User  # Assuming you have a User model
from app.extensions import db

@pytest.fixture
def client():
    # Create a test Flask app
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory SQLite database for testing

    # Set up the database
    with app.app_context():
        db.create_all()

    # Create a test client
    with app.test_client() as client:
        yield client

    # Tear down the database after the test
    with app.app_context():
        db.drop_all()

def test_register_user(client):
    # Test user registration
    response = client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 201
    assert response.json == {'msg': 'User registered successfully'}

def test_login_user(client):
    # Register a user first
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })

    # Test user login
    response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_protected_route(client):
    # Register and login a user
    client.post('/api/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    login_response = client.post('/api/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })
    access_token = login_response.json['access_token']

    # Test accessing a protected route
    response = client.get('/api/auth/protected', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200
    # assert response.json == {'message': 'You are accessing a protected route'}

def test_protected_route_without_token(client):
    # Test accessing a protected route without a token
    response = client.get('/api/auth/protected')
    assert response.status_code == 401
    assert response.json == {'msg': 'Missing Authorization Header'}

def test_protected_route_with_invalid_token(client):
    # Test accessing a protected route with an invalid token
    response = client.get('/api/auth/protected', headers={
        'Authorization': 'Bearer invalidtoken'
    })
    assert response.status_code == 422
    assert response.json == {'msg': 'Not enough segments'}