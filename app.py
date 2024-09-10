from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client['demo_registrationDB']
registration_collection = db['registration']

@app.route('/register', methods=['POST'])
def register():
    print("received")
    
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    # Check if the username already exists
    existing_user = registration_collection.find_one({"username": username})
    if existing_user:
        return jsonify({"message": "Username already exists!"}), 400

    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Insert new user into MongoDB
    new_user = {"username": username, "password": hashed_password}
    result = registration_collection.insert_one(new_user)

    return jsonify({"message": "User registered successfully!", "user_id": str(result.inserted_id)}), 201

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message" : "tested successfully"})

@app.route('/users', methods=['GET'])
def get_users():
    users = []

    for user in registration_collection.find():
        users.append({"id": str(user["_id"]), "username": user["username"]})
    
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
