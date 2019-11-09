import dateutil.parser
from flask import Blueprint, Response, jsonify, request
from LiftSmartApp.db.databaseAccessor import DatabaseAccessor

db = DatabaseAccessor()
mod = Blueprint('exercise_management', __name__)

@mod.route("/add-set", methods=["POST"])
def add_set():
    arguments = request.json
    username = arguments['username']
    exercise_name = arguments['exercise_name']
    reps = arguments['reps']
    weight = arguments['weight']

    newSet = db.addSet(username, exercise_name,reps,weight)
    return jsonify(newSet)

@mod.route("/delete-set", methods=["DELETE"])
def delete_set():
    username = request.args.get('username')
    exercise_name = request.args.get('exercise_name')
    time_performed = dateutil.parser.parse(request.args.get('time_performed'))

    deletedSet = db.deleteSet(username, exercise_name, time_performed)
    return f"{deletedSet}"

@mod.route("/get-all-sets", methods = ["GET"])
def get_all_sets():
    username = request.args.get("username")
    allSets = db.getAllSets(username)
    return jsonify(allSets)

@mod.route("/get-all-exercise-types",methods = ["GET"])
def get_all_exercise_types():
    allExercises = db.getAllExerciseTypes()
    return jsonify(allExercises)


