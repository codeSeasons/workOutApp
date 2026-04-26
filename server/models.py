from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from marshmallow import Schema, fields, validate


metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)


class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    workout_exercises = db.relationship(
        "WorkoutExercises",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )

    workouts = association_proxy("workout_exercises", "workout")

    @validates("name")
    def validate_name(self, key, name):
        if not name or not name.strip():
            raise ValueError("Exercise must have a name.")
        return name

    @validates("category")
    def validate_category(self, key, category):
        if not category or not category.strip():
            raise ValueError("Exercise must have a category.")
        return category

    def __repr__(self):
        return f"<Exercise {self.id}: {self.name}>"


class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)

    workout_exercises = db.relationship(
        "WorkoutExercises",
        back_populates="workout",
        cascade="all, delete-orphan"
    )

    exercises = association_proxy("workout_exercises", "exercise")

    @validates("duration_minutes")
    def validate_duration_minutes(self, key, duration_minutes):
        if duration_minutes is None or duration_minutes <= 0:
            raise ValueError("Workout duration_minutes must be greater than 0.")
        return duration_minutes

    @validates("notes")
    def validate_notes(self, key, notes):
        if notes and len(notes) > 250:
            raise ValueError("Workout notes must be 250 characters or fewer.")
        return notes

    def __repr__(self):
        return f"<Workout {self.id}: {self.date}, {self.duration_minutes} minutes>"


class WorkoutExercises(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        db.ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey("exercises.id"),
        nullable=False
    )

    reps = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False)

    workout = db.relationship(
        "Workout",
        back_populates="workout_exercises"
    )

    exercise = db.relationship(
        "Exercise",
        back_populates="workout_exercises"
    )

    @validates("reps", "sets", "duration_seconds")
    def validate_positive_integer(self, key, value):
        if value is None or value <= 0:
            raise ValueError(f"{key} must be greater than 0.")
        return value

    def __repr__(self):
        return (
            f"<WorkoutExercises workout_id={self.workout_id}, "
            f"exercise_id={self.exercise_id}, reps={self.reps}, "
            f"sets={self.sets}, duration_seconds={self.duration_seconds}>"
        )
    
class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.String(
        required=True,
        validate=validate.Length(min=1, error="Exercise name is required.")
    )

    category = fields.String(
        required=True,
        validate=validate.Length(min=1, error="Exercise category is required.")
    )

    equipment_needed = fields.Boolean(required=True)

    workout_exercises = fields.Nested(
        lambda: WorkoutExercisesSchema(exclude=("exercise",)),
        many=True,
        dump_only=True
    )


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)

    date = fields.Date(required=True)

    duration_minutes = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Duration must be greater than 0.")
    )

    notes = fields.String(
        validate=validate.Length(max=250, error="Notes must be 250 characters or fewer.")
    )

    workout_exercises = fields.Nested(
        lambda: WorkoutExercisesSchema(exclude=("workout",)),
        many=True,
        dump_only=True
    )


class WorkoutExercisesSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    reps = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Reps must be greater than 0.")
    )

    sets = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Sets must be greater than 0.")
    )

    duration_seconds = fields.Int(
        required=True,
        validate=validate.Range(min=1, error="Duration seconds must be greater than 0.")
    )

    workout = fields.Nested(
        lambda: WorkoutSchema(exclude=("workout_exercises",)),
        dump_only=True
    )

    exercise = fields.Nested(
        lambda: ExerciseSchema(exclude=("workout_exercises",)),
        dump_only=True
    )