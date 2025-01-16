from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

users_db = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_db), 200

@app.route('/users/<int:user_id>', methods=['GET']) 
def get_user(user_id):
    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return abort(404)
    return jsonify(user), 200

@app.route('/users', methods=['POST']) 
def create_user():
    if not request.is_json:
        return abort(400)

    data = request.get_json()
    if 'name' not in data or 'lastname' not in data:
        return abort(400)

    new_id = len(users_db) + 1
    user = {
        "id": new_id,
        "name": data['name'],
        "lastname": data['lastname']
    }
    users_db.append(user)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return abort(404)

    data = request.get_json()
    if not data or ('name' not in data and 'lastname' not in data):
        return abort(400)

    if 'name' in data:
        user['name'] = data['name']
    if 'lastname' in data:
        user['lastname'] = data['lastname']

    return '', 204

@app.route('/users/<int:user_id>', methods=['PUT'])
def replace_user(user_id):
    if not request.is_json:
        return abort(400)

    data = request.get_json()
    if 'name' not in data or 'lastname' not in data:
        return abort(400)

    user = next((user for user in users_db if user['id'] == user_id), None)
    if user is None:
        return abort(404)

    user.update(data)
    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    global users_db
    if any(user['id'] == user_id for user in users_db):
        users_db = [user for user in users_db if user['id'] != user_id]
        return '', 204
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True)
