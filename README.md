Here’s the complete and well-formatted `README.md` file for your Flask JWT Authentication project:

---

# Flask JWT Authentication with MySQL

This is a production-ready Flask application that implements JWT-based authentication using MySQL as the database.

---

## Project Structure

```
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
│   └── open_routes.py
│
├── tests/
│   ├── __init__.py
│   └── test_auth.py
│   └── test_open_route.py
│
├── requirements.txt
├── run.py
└── README.md
```

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-jwt-app.git
cd flask-jwt-app
```

### 2. Set Up Virtual Environment

Create a virtual environment:

```bash
python3 -m venv flask-jwt-app
```

Activate the virtual environment:

- On macOS/Linux:
  ```bash
  source flask-jwt-app/bin/activate
  ```
- On Windows:
  ```bash
  flask-jwt-app\Scripts\activate
  ```

### 3. Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up MySQL Database

1. Create a MySQL database named `flask_jwt_app`.
2. Update the `SQLALCHEMY_DATABASE_URI` in `app/config.py` with your MySQL credentials:
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/flask_jwt_app'
   ```

### 5. Run Migrations

Create the database tables:

```bash
flask shell
>>> from app.extensions import db
>>> db.create_all()
```

### 6. Run the Application

Start the Flask development server:

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. Register a User

```bash
curl -X POST http://127.0.0.1:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
```

### 2. Login and Get a JWT

```bash
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpassword"}'
```

### 3. Get All Users (Protected Route)

```bash
curl -X GET http://127.0.0.1:5000/api/auth/users \
  -H "Authorization: Bearer <your_jwt_token>"
```

### 4. Get a Specific User by ID (Protected Route)

```bash
curl -X GET http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>"
```

### 5. Update a User (Protected Route)

```bash
curl -X PUT http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>" \
  -H "Content-Type: application/json" \
  -d '{"username": "updateduser", "role": "admin"}'
```

### 6. Delete a User (Protected Route)

```bash
curl -X DELETE http://127.0.0.1:5000/api/auth/users/1 \
  -H "Authorization: Bearer <your_jwt_token>"
```

### 7. Access Protected Route

```bash
curl -X GET http://127.0.0.1:5000/api/auth/protected \
  -H "Authorization: Bearer <your_jwt_token>"
```

### 7. Access Open Route

```bash
curl -X GET http://127.0.0.1:5000/api/welcome
```

Response:

```json
{
    "message": "Welcome to the open route!"
}
```

---

## How to Share Project Dependencies

Instead of sharing the virtual environment, share the project dependencies using a `requirements.txt` file. Developers can recreate the virtual environment using this file.

### Generate `requirements.txt`

Run the following command to generate a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### Install Dependencies

Other developers can install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Running the Tests

```bash
pip install pytest
```

Run all test:

```bash
pytest
```

To run test for indiviadual file rub below command:

```bash
pytest tests/test_auth.py
pytest tests/test_open_routes.py
```

---


## Best Practices

1. **Exclude Virtual Environment Files**: Add `venv/`, `env/`, and `.venv/` to your `.gitignore` file.
2. **Environment Variables**: Store sensitive information (e.g., database credentials, JWT secret key) in environment variables and exclude `.env` files from Git.
3. **Documentation**: Keep the `README.md` file updated with setup instructions and API documentation.

---

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the [LICENSE](LICENSE) file for details.

