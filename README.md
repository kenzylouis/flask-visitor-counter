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
views import the Flask Blueprint module to build blueprints of the app

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
"You need to be able to see the models from your application.py

need to do ```from counter.models import Counter``` in the views file im order for the app to be able to create migrations to the DB - Link the views(controller) and Models.

for the the 1st time ```flask db init```
then ```flask db migrate```
then ```flask db upgrade```

Steps 5
--------
perfrom Database operations from the shell (CRUD)

```flask shell```
perform CRUD operations. Through the SQLAlchemy you can perform query to the DB

```python
from counter.models import Counter
from application import db
Counter.query.all
```
counter is a representation of the DB

## Create a record into the DB

To right our 1st record in the DB:
```counter = Counter(count=1)```

but this value is not in the DB yet. SQLAlchemy has this concept of a session
to verify it is not yet written to the DB:
```counter.id```
it writes after a session to the DB is created. A session is a series of DB operaions that are related together, that are written/commited to the DB once we have all the necessary ones.
```db.session.add(counter)```

benefits: 
1. no need to write all operations individually, but can do all of them with one DB call
2. we can rollback easily if something goes wrong
to commit:
```db.session.commit()```
now check the counter table
```counter.id```

## Read a record from the DB
### by ID

```python
counter_1 = Counter.query.get(1)
counter_1
<Count 1>
```
the return value `<Count 1>` is the __repr__ of our class Counter

we can also get the value of count
```counter_1.count```

### query all
we can query all like this:
```python
counter_list = Counter.query.all()
counter_2 = counter_list[0]
counter_2
```
shoud return:
`<Count 1>`

if we need the first element in the Table:

```
counter_2 = Counter.query.first()
counter_2
<Count 1>
```
## Update a record in the DB

get the value:

`counter = Counter.query.get(1)`

verify
`counter.count`

set the value of count to 2:
`counter.count = 2`

to update the record in DB, no need to add the the DB session, b/c SQLAlchemy already have an ID for the record

to write the update:
`db.session.commit()`

## Delete a record from the DB

Fetch it first and execute a delete on the object:
```python
counter = Counter.query.get(1)
db.session.delete(counter)
db.session.commit()

```
verify DB is empty
`Counter.query.all()`

Steps 6
-------

Create the page views for the application

* had to install cryptography because of the following error:

`RuntimeError: cryptography is required for sha256_password or caching_sha2_password`

did a : `pip install cryptography`

Step 7
------

## Testing suite for the app
modify the application.py to add overrides to the app so we can overrides the settings when running the test

Add KW Args call `**config_overrides`, then update app.config

Why do we need a separate DB for the test? so we don't mess up the existing main DB, also we want the code to run with fresh data every time we run the test, to avoid having left over data that mess up the validity of the test case 

we also want utility script that does that for us so we don't have to repeat code in our app

it creates and drop a test DB, test_db.py

and inside my app folder, there is a tests.py file that test the application

create a test class in the test file. test files are organized by classes with corresponding tests. we can have more than 1 classes

we have requiered method like `setUp` and `tearDown`, providing fresh version of the app for each type of test
- instantiate the Test DB with the utility, and get the conn from it
- create an instance of the app and store it in an app factory. This is another create_app method with the setting overrides of the test
- `TESTING = True`:  in testing mode, flask disables the error catching during request handling for better error reports when performing test request against the app, that increase perfomrance too. The SQL alchemy db uri is the one returned by our test db utility. once we have the factory we create the app
- sql aclhemy provides method to create app tables without using migrations: `create_all()` and `drop_all()`
- `app_context()`: simulates all that is in the with block as if we were in Flask and execute the code like flask run. All operations in a view are in the `app_context()`

Step 8
------

each needs to begin with `test_` so that the unittest library can run the `setUp` and `tearDown` before and after it

This is what test boiles down to: asserting or making sure that something we are expecting to be happening is happening. if the result is false, the test is not passing

add the tests.py file under the root folder. It will automatically discover all the tests.py file in all the app folders in the application