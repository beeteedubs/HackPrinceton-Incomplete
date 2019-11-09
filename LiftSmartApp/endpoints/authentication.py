from flask import Blueprint, Response, json, request
from LiftSmartApp.db.databaseAccessor import DatabaseAccessor

db = DatabaseAccessor()
mod = Blueprint('authentication', __name__)

@mod.route("/create-user", methods=["POST"])
def create_user():
    print(request.data)
    arguments = request.json
    username = arguments['username']
    password = arguments['password']

    newUser = db.createUser(username,password)

    return f"{newUser}"

@mod.route("/login-user", methods=["GET"])
def login_user():
    username = request.args.get("username")
    password = request.args.get("password")

    isUser = db.loginUser(username, password)
    return f"{isUser}"


