# workOutApp
API_crud


# Work Out App

## Installation Instructions

Clone the project and move into the server folder.

```bash
cd server

Install dependencies.

pipenv install

Start the virtual environment.

pipenv shell

Run migrations.

flask db init
flask db migrate -m "Create workout app tables"
flask db upgrade

Seed the database.

python seed.py

Start the Flask server.

python app.py

The app should run at:

http://localhost:5555
Description

This is a simple Flask workout tracking app. It uses SQLAlchemy models to keep track of workouts, exercises, and the exercises connected to each workout.

The app has three main models:

Exercise
Workout
WorkoutExercises

A workout can have many exercises, and an exercise can belong to many workouts through the WorkoutExercises join table.

Models
Exercise

Stores information about an exercise.

id
name
category
equipment_needed
Workout

Stores information about a workout.

id
date
duration_minutes
notes
WorkoutExercises

This is the join table between workouts and exercises.

id
workout_id
exercise_id
reps
sets
duration_seconds
Validations

Some validations were added to help keep the data clean.

Exercise name cannot be blank
Exercise category cannot be blank
Workout duration must be greater than 0
Workout notes must be 250 characters or fewer
Reps, sets, and duration seconds must be greater than 0
Routes
GET /workouts
GET /workouts/<id>
POST /workouts
DELETE /workouts/<id>

GET /exercises
GET /exercises/<id>
POST /exercises
DELETE /exercises/<id>

POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises


Run Instructions

After installation, start the server with:

python app.py

Then open this in the browser:

http://localhost:5555/
Project Status

This project currently has the models, relationships, seed data, routes, and schemas started. More route functionality can be added after serialization is fully connected.