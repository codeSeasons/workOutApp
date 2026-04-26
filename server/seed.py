#!/usr/bin/env python3

from app import app
from models import *
from datetime import date

with app.app_context():
    db.create_all()

    # Delete association/join records first so foreign keys do not complain
    WorkoutExercises.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    # 10 Exercise examples
    exercise1 = Exercise(name='pullup', category='back', equipment_needed=False)
    exercise2 = Exercise(name='pushup', category='chest', equipment_needed=False)
    exercise3 = Exercise(name='squat', category='legs', equipment_needed=False)
    exercise4 = Exercise(name='bench press', category='chest', equipment_needed=True)
    exercise5 = Exercise(name='deadlift', category='back', equipment_needed=True)
    exercise6 = Exercise(name='plank', category='core', equipment_needed=False)
    exercise7 = Exercise(name='bicep curl', category='arms', equipment_needed=True)
    exercise8 = Exercise(name='lunges', category='legs', equipment_needed=False)
    exercise9 = Exercise(name='shoulder press', category='shoulders', equipment_needed=True)
    exercise10 = Exercise(name='jump rope', category='cardio', equipment_needed=True)

    db.session.add_all([
        exercise1,
        exercise2,
        exercise3,
        exercise4,
        exercise5,
        exercise6,
        exercise7,
        exercise8,
        exercise9,
        exercise10
    ])

    # 10 Workout examples
    workout1 = Workout(date=date(2026, 4, 1), duration_minutes=20, notes='Light back workout')
    workout2 = Workout(date=date(2026, 4, 2), duration_minutes=25, notes='Chest and arms')
    workout3 = Workout(date=date(2026, 4, 3), duration_minutes=30, notes='Leg day')
    workout4 = Workout(date=date(2026, 4, 4), duration_minutes=45, notes='Heavy chest workout')
    workout5 = Workout(date=date(2026, 4, 5), duration_minutes=50, notes='Deadlift focus')
    workout6 = Workout(date=date(2026, 4, 6), duration_minutes=15, notes='Core training')
    workout7 = Workout(date=date(2026, 4, 7), duration_minutes=35, notes='Arm pump workout')
    workout8 = Workout(date=date(2026, 4, 8), duration_minutes=30, notes='Lower body endurance')
    workout9 = Workout(date=date(2026, 4, 9), duration_minutes=40, notes='Shoulder strength')
    workout10 = Workout(date=date(2026, 4, 10), duration_minutes=20, notes='Cardio finisher')

    db.session.add_all([
        workout1,
        workout2,
        workout3,
        workout4,
        workout5,
        workout6,
        workout7,
        workout8,
        workout9,
        workout10
    ])

    # 10 WorkoutExercises examples
    workoutExercises1 = WorkoutExercises(
        workout=workout1,
        exercise=exercise1,
        reps=10,
        sets=3,
        duration_seconds=60
    )

    workoutExercises2 = WorkoutExercises(
        workout=workout2,
        exercise=exercise2,
        reps=15,
        sets=4,
        duration_seconds=90
    )

    workoutExercises3 = WorkoutExercises(
        workout=workout3,
        exercise=exercise3,
        reps=12,
        sets=3,
        duration_seconds=75
    )

    workoutExercises4 = WorkoutExercises(
        workout=workout4,
        exercise=exercise4,
        reps=8,
        sets=5,
        duration_seconds=120
    )

    workoutExercises5 = WorkoutExercises(
        workout=workout5,
        exercise=exercise5,
        reps=6,
        sets=4,
        duration_seconds=150
    )

    workoutExercises6 = WorkoutExercises(
        workout=workout6,
        exercise=exercise6,
        reps=30,
        sets=3,
        duration_seconds=180
    )

    workoutExercises7 = WorkoutExercises(
        workout=workout7,
        exercise=exercise7,
        reps=12,
        sets=4,
        duration_seconds=80
    )

    workoutExercises8 = WorkoutExercises(
        workout=workout8,
        exercise=exercise8,
        reps=20,
        sets=3,
        duration_seconds=100
    )

    workoutExercises9 = WorkoutExercises(
        workout=workout9,
        exercise=exercise9,
        reps=10,
        sets=5,
        duration_seconds=110
    )

    workoutExercises10 = WorkoutExercises(
        workout=workout10,
        exercise=exercise10,
        reps=50,
        sets=2,
        duration_seconds=300
    )

    db.session.add_all([
        workoutExercises1,
        workoutExercises2,
        workoutExercises3,
        workoutExercises4,
        workoutExercises5,
        workoutExercises6,
        workoutExercises7,
        workoutExercises8,
        workoutExercises9,
        workoutExercises10
    ])

    db.session.commit()

    print("Database seeded successfully!")