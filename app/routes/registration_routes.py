from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, get_all_users
from app.middlewares.validation import validate_registration_data

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
@validate_registration_data
def register():
    try:
        data = request.get_json()
        response, status = register_user(data)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@registration_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = get_all_users()
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@registration_bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Service is running"}), 200
