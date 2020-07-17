#create new super user
python3 manage.py createsuperuser
#enter username
#enter Email
#enter Password

#add json file to database
python3 manage.py shell 
>>> import json
>>> from app.models import Exercise
>>> with open('Exercises.json') as f:
...     exer_json = json.load(f)
...
>>> for exe in exer_json:
...     exercise = Exercise(name=exe['name'], group=exe['group'], group_code=exe['group_code'], description=exe['description'], image_link=exe['image_link'])
...     exercise.save()
...
>>> exit()