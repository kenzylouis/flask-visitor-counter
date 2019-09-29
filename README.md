Step 1
-------
create folder
create venv
git init
pip install requirements
create .gitignore
create .flaskenv
create settings.py
create application.py (application factory to instantiate my app)
create manage.py
blueprints

Steps 2
-------
create counter folder
under counter, create __init__.py and views.py
update the application.py, import the app from counter.views
then register the app

Steps 3
-------
Build model to define the modules schema. have many class that represent tables in the Database
create a file in counter dir called models.py
import the SQLALchemy db instance from application to the model
define Class, as an extension of the SQLACLHEMY DB instance Model Class
class will have an ID and a counter as an Integer
class will have an init method (__init__) - will be called when creating the object for the 1st time
All classes have a reproduce/represent method (__repr__), how they are printed in the terminal when creating a record 

Steps 4
-------

Migrate to database using flask-migrate -  there are 4 command to remember
- init : 1st timer 
- migrate: checks all changes in models and save them in migrations file
- upgrade: apply the latest migration file change to the DB
- Downgrade: revert the latest change in the DB to the previous one before it.

Models Dicsovery for Migrations (VERY IMP.)
"You need to be apble to see the models from your application.py

need to do ```from counter.models import Counter``` in the views file im order for the app to be able to create migrations to the DB - Link the views(controller) and Models.

for the the 1st time ```flask db init```
then ```flask db migrate```
then ```flask db upgrade```


here are



