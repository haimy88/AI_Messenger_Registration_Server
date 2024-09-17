from flask import current_app
import bcrypt

def register_user(data):
    username = data.get('username')
    password = data.get('password')

    registration_collection = current_app.db['registration']

    existing_user = registration_collection.find_one({"username": username})
    if existing_user:
        return {"message": "Username already exists!"}, 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    new_user = {"username": username, "password": hashed_password}
    result = registration_collection.insert_one(new_user)

    return {"message": "User registered successfully!", "user_id": str(result.inserted_id)}, 201

def get_all_users():
    registration_collection = current_app.db['registration']

    users = []
    for user in registration_collection.find():
        users.append({"id": str(user["_id"]), "username": user["username"]})

    return users
