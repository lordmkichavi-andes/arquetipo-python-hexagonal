from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from presentation.dtos.user_dto import UserDTO

user_bp = Blueprint("user_bp", __name__)

create_user_use_case = None
get_user_use_case = None

def init_use_cases(create_uc, get_uc):
    global create_user_use_case, get_user_use_case
    create_user_use_case = create_uc
    get_user_use_case = get_uc

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        dto = UserDTO(**data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    user = create_user_use_case.execute(dto.name, dto.email)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": str(user.created_at)
    }), 201

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    user = get_user_use_case.get_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": str(user.created_at)
    }), 200

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = get_user_use_case.get_all()
    return jsonify([
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "created_at": str(u.created_at)
        }
        for u in users
    ]), 200
