from flask import Blueprint, request, jsonify
from app.services.auth_service import register_user, get_all_users

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    response, status = register_user(data)
    return jsonify(response), status

@registration_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@registration_bp.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "tested successfully"})
