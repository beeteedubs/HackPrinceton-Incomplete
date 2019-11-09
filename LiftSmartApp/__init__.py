from flask import Flask
from LiftSmartApp.endpoints import authentication, exercise_management

app = Flask(__name__)
app.secret_key = "ssshhh... this is secret"

app.register_blueprint(authentication.mod)
app.register_blueprint(exercise_management.mod)