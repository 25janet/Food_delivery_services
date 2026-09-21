from flask import Flask,jsonify
from app.database.connection import db, get_database_url
from app.models.user import User

app = Flask(__name__)

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#initialize the database
db.init_app(app)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify(
        {"service": "User service"},
        {"status": "healthy"}
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
    app.run(host='0.0.0.0',port=5000)