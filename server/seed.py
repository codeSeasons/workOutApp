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

    # 10 WorkoutExercises examples
    workoutExercises1 = WorkoutExercises(date='2026-04-01', duration_minutes=20, notes='Light back workout')
    workoutExercises2 = WorkoutExercises(date='2026-04-02', duration_minutes=25, notes='Chest and arms')
    workoutExercises3 = WorkoutExercises(date='2026-04-03', duration_minutes=30, notes='Leg day')
    workoutExercises4 = WorkoutExercises(date='2026-04-04', duration_minutes=45, notes='Heavy chest workout')
    workoutExercises5 = WorkoutExercises(date='2026-04-05', duration_minutes=50, notes='Deadlift focus')
    workoutExercises6 = WorkoutExercises(date='2026-04-06', duration_minutes=15, notes='Core training')
    workoutExercises7 = WorkoutExercises(date='2026-04-07', duration_minutes=35, notes='Arm pump workout')
    workoutExercises8 = WorkoutExercises(date='2026-04-08', duration_minutes=30, notes='Lower body endurance')
    workoutExercises9 = WorkoutExercises(date='2026-04-09', duration_minutes=40, notes='Shoulder strength')
    workoutExercises10 = WorkoutExercises(date='2026-04-10', duration_minutes=20, notes='Cardio finisher')

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

    # 10 Workout examples
    workout1 = Workout(reps=10, sets=3, duration_seconds=60)
    workout2 = Workout(reps=15, sets=4, duration_seconds=90)
    workout3 = Workout(reps=12, sets=3, duration_seconds=75)
    workout4 = Workout(reps=8, sets=5, duration_seconds=120)
    workout5 = Workout(reps=6, sets=4, duration_seconds=150)
    workout6 = Workout(reps=30, sets=3, duration_seconds=180)
    workout7 = Workout(reps=12, sets=4, duration_seconds=80)
    workout8 = Workout(reps=20, sets=3, duration_seconds=100)
    workout9 = Workout(reps=10, sets=5, duration_seconds=110)
    workout10 = Workout(reps=50, sets=2, duration_seconds=300)

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

    db.session.commit()

    print("Database seeded successfully!")