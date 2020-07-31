# FitTrack

## For Production Release
Link to GitHub repo - https://github.com/kdagnan/FitTrack.git  
FitTrack is a web app where users can track all aspects of their fitness: including exercises, weight, and caloric intake. Users can then track their progess on strength gains, caloric intake, and weight history visually with graphs.  

1. Unarchive FitTrack.tgz (tar -xvzf FitTrack.tgz)
2. "pip install ." to install all dependencies outlined in the setup.py
2. Execute init.py to initialize project and create sqlite database
3. Execute run.py file to run server on localhost:8000

Note: If you try to sign up and are not redirected to the log in page, make sure your password meets these requirements:
 - Your password cannot be too similar to your other personal information
 - Your password must contain at least 8 characters
 - Your password can't be a commonly used password
 - Your password can't be entirely numeric
 - The two password fields must match

## Setting Up Through Cloning Repo
1. Create a venv (https://docs.python.org/3/tutorial/venv.html)
2. Git Clone (https://github.com/kdagnan/FitTrack.git) into Django directory in venv directory
3. Install Django (python -m pip install Django)
4. Run python manage.py migrate
5. Run python manage.py runserver
6. Visit localhost:8000
7. Try to push a commit just to test.

#### Example of Filesystem After Setup
![image](https://i.imgur.com/ZMN1sl0.png)
