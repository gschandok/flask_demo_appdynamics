from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


@app.route("/<count>")
def hello_world(count):
    users = User.query.all()
    return jsonify(hello=" there!! Total Users registered are " + len(users))

@app.route('/users', methods=['POST', 'GET'])
def handle_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = User(email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"New User with emailId, {new_user.email} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        users = User.query.all()
        results = [
            {
                "userId": user.id,
                "email": user.email,
                "active": user.active
            } for user in users]

        return {"count": len(results), "users": results}