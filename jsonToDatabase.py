# Run this file with:
# python manage.py shell < jsonToDatabase.py

# Add Exercises from json file to database
import json
from app.models import Exercise
with open('Exercises.json') as f:
    exer_json = json.load(f)

for exe in exer_json:
    exercise = Exercise(name=exe['name'], group=exe['group'], group_code=exe['group_code'], description=exe['description'], image_link=exe['image_link'], ex_id=exe['ex_id'])
    exercise.save()
