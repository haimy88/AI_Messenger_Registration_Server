from functools import wraps
from flask import request, jsonify
import re

def validate_registration_data(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            data = request.get_json()

            if not data or 'username' not in data or 'password' not in data:
                return jsonify({"message": "Missing required fields: username (valid email) and password"}), 400

            if len(data['password']) < 6:
                return jsonify({"message": "Password must be at least 6 characters long"}), 400

            if not is_valid_email(data['username']):
                return jsonify({"message": "Username must be a valid email address"}), 400

            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": f"An error occurred during validation: {str(e)}"}), 500

    return decorated_function

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)
