# Flask JWT Authentication with MySQL

This is a production-ready Flask application that implements JWT-based authentication using MySQL as the database.

flask-jwt-app/
│
├── app/
│   ├── __init__.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── services.py  # Auth-related business logic
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py      # User model and related methods
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py  # User-related business logic
│   ├── config.py
│   └── extensions.py
│
├── tests/
│   ├── __init__.py
│   └── test_auth.py
│
├── requirements.txt
├── run.py
└── README.md

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask-jwt-app.git
   cd flask-jwt-app

1a. *setup virtual env*
python3 -m venv flask-jwt-app

1b. *Activate virtual env:*
source flask-jwt-app/bin/activate


2. **Install dependencies:**

pip install -r requirements.txt

3. **Run migrations:**
flask shell
>>> from app.extensions import db
>>> db.create_all()

4. **Run the application:**

python run.py

**How to Share Project Dependencies**

Instead of sharing the virtual environment, share the project dependencies using a requirements.txt file. Developers can recreate the virtual environment using this file.

5. Run the following command to generate a requirements.txt file:

pip freeze > requirements.txt

Example: 

1. Register:
curl -X POST http://127.0.0.1:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'

2. Login to Get a JWT
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'

3. Get All Users
curl -X GET http://127.0.0.1:5000/api/auth/users \
  -H "Authorization: Bearer <your_jwt_token>"

4. Get a Specific User by ID
curl -X GET http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>"

5. Update a User
curl -X PUT http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>" \
  -H "Content-Type: application/json" \
  -d '{"username": "updateduser", "role": "admin"}'

6. Delete a User
curl -X DELETE http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>"

7. protected:
curl -X GET http://127.0.0.1:5000/api/auth/protected \
  -H "Authorization: Bearer <your_jwt_token>"