from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from marshmallow import Schema, fields
from datetime import date


metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)
# Define Models here

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)

    # Exercise has many WorkoutExercises
    workout_exercises = db.relationship(
        "WorkoutExercises",
        back_populates="exercise"
    )

    # Exercise has many Workouts through WorkoutExercises
    workouts = db.relationship(
        "Workout",
        secondary="workout_exercises",
        back_populates="exercises",
        viewonly=True
    )

    def __repr__(self):
        return f"<Exercise {self.id}: {self.name}>"

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    duration_minutes = db.Column(db.Integer)
    notes = db.Column(db.String)

    # Workout has many WorkoutExercises
    workout_exercises = db.relationship(
        "WorkoutExercises",
        back_populates="workout"
    )

    # Workout has many Exercises through WorkoutExercises
    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercises",
        back_populates="workouts",
        viewonly=True
    )

    def __repr__(self):
        return f"<Workout {self.id}: {self.date}>"

class WorkoutExercises(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # WorkoutExercise belongs to a Workout
    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    # WorkoutExercise belongs to an Exercise
    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    def __repr__(self):
        return f"<WorkoutExercises workout_id={self.workout_id}, exercise_id={self.exercise_id}>"