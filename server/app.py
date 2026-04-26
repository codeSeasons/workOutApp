from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


# Define Routes here
@app.route('/')
def index():
    return '<h1>Work Out App</h1>'


# GET /workouts
# List all workouts
@app.route('/workouts', methods=['GET'])
def get_workouts():
    return jsonify({"message": "List all workouts"}), 200


# GET /workouts/<id>
# Show a single workout with its associated exercises
@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout_by_id(id):
    return jsonify({"message": f"Show workout {id}"}), 200


# POST /workouts
# Create a workout
@app.route('/workouts', methods=['POST'])
def create_workout():
    return jsonify({"message": "Create a workout"}), 201


# DELETE /workouts/<id>
# Delete a workout
@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    return jsonify({"message": f"Delete workout {id}"}), 200


# GET /exercises
# List all exercises
@app.route('/exercises', methods=['GET'])
def get_exercises():
    return jsonify({"message": "List all exercises"}), 200


# GET /exercises/<id>
# Show an exercise and associated workouts
@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise_by_id(id):
    return jsonify({"message": f"Show exercise {id}"}), 200


# POST /exercises
# Create an exercise
@app.route('/exercises', methods=['POST'])
def create_exercise():
    return jsonify({"message": "Create an exercise"}), 201


# DELETE /exercises/<id>
# Delete an exercise
@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercise(id):
    return jsonify({"message": f"Delete exercise {id}"}), 200


# POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
# Add an exercise to a workout, including reps/sets/duration
@app.route(
    '/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises',
    methods=['POST']
)
def create_workout_exercise(workout_id, exercise_id):
    return jsonify({
        "message": f"Add exercise {exercise_id} to workout {workout_id}"
    }), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)