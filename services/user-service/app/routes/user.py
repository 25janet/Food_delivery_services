from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from app.database.connection import db
from app.models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/users/register", methods=["POST"])
def register_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 400
    password_hash = generate_password_hash(password)

    new_user = User(name=name, email=email, password_hash=password_hash)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfuly",
                    "user": {"id": new_user.id,
                             "name": new_user.name,
                             "email": new_user.email}}), 201
