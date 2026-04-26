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
    __tablename__='exercises'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    equipment_needed = db.Column(db.Boolean)


    def __repr__(self):
        return f"<Exercise {self.id}, {self.name}, {self.equipment_needed}>"
    


class Workout(db.Model):
    __tablename__='workouts'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String) #probably wrong, use date import?
    duration_minutes = db.Column(db.integer)
    notes = db.Column(db.String)


    def __repr__(self):
        return f"<Workout {self.id}, {self.date}, {self.duration_minutes}, {self.notes}>"
    


class WorkoutExercises(db.Model):
    __tablename__='workout_exercises'
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workouut.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id"))
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    def __repr__(self):
        return (
               f"<WorkoutExercises {self.id}, Workout{self.workout_id}, " 
               f"Exercise{self.exercise_id}, {self.reps}, {self.sets}, {self.duration_seconds}>"
        )
