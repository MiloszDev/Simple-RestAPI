# Simple-RestAPI
This project is a **basic REST API** built using **Flask**, designed to manage user data. It demonstrates essential CRUD operations and is ideal for small-scale applications or learning purposes.

---

## Features

- **GET** `/users`: Retrieve all users.
- **GET** `/users/<user_id>`: Retrieve a single user by ID.
- **POST** `/users`: Create a new user.
- **PATCH** `/users/<user_id>`: Update specific user fields.
- **PUT** `/users/<user_id>`: Replace a user entirely.
- **DELETE** `/users/<user_id>`: Remove a user by ID.

---

## Setup and Usage

1. **Clone the repository**:
    
    ```bash
    git clone https://github.com/yourusername/simple-flask-restapi.git
    cd simple-flask-restapi
    ```
    
2. **Install dependencies**:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. **Run the application**:
    
    ```bash
    python app.py
    ```
    
4. **API Endpoints**:
    - Access the API at `http://127.0.0.1:5000`.
    - Use tools like **Postman**, **curl**, or your browser to interact with the API.

---

## Example Request

### Create a User

**POST** `/users`

Body (JSON):

```json
{
  "name": "John",
  "lastname": "Doe"
}
```

Response:

```json
{
  "id": 1,
  "name": "John",
  "lastname": "Doe"
}
```

---

## Tests

Unit tests are provided to ensure API functionality. To run tests:

```bash
python -m unittest test_app.py
```

---

## Limitations

- **In-Memory Database**: Data is not persistent and resets on server restart.
- **No Authentication**: This API is open and unauthenticated.
- **Simple Validation**: Basic error handling and input validation.

---

## License

This project is licensed under the MIT License. Feel free to use and modify it for your projects!
