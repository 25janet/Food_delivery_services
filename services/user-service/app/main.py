from flask import Flask,jsonify
from importlib import import_module

JWTManager = import_module("flask_jwt_extended").JWTManager
from app.database.connection import db, get_database_url
from app.models.user import User
from app.routes.user import user_bp


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "dev-secret-key"
jwt = JWTManager(app)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize the database
db.init_app(app)

app.register_blueprint(user_bp, url_prefix="/api")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(
        {"service": "User service",
        "status": "healthy"}
    )
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "message": "User endpoint is working"
        }
    )

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5001)