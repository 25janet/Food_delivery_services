from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity,jwt_required  # type: ignore[reportMissingImports]
from werkzeug.security import generate_password_hash,check_password_hash

from app.database.connection import db
from app.models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "error": "Name, email, and password are required"
        }), 400

    email = email.strip().lower()

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "error": "User with this email already exists"
        }), 409

    password_hash = generate_password_hash(password)

    new_user = User(
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }), 201


@user_bp.route("/users/login", methods=["POST"])
def login_user():
    data = request.get_json()

    if  data is None:
        return jsonify({
            "error": "Request body must contain JSON"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and password are required"
        }), 400

    email = email.strip().lower()

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    if not check_password_hash(user.password_hash, password):
        return jsonify({
            "error": "Invalid email or password"
        }), 401

    access_token = create_access_token(identity=str(user.id))

    return jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200


@user_bp.route("/users/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "User not found"
        }), 404

    return jsonify({
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
    }), 200