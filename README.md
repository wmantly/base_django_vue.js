# django
## Getting started

* Clone
* Start the virtual env `source env/bin/activate`
* Install dependencies `pip install -r requirements.txt`
* Migrate the database `./manage.py migrate`
* start dev server `./manage.py runserver`

## Updating the database

When a model is changed the databse needs to be migrated. To do this run `./manage.py makemigrations` to stage the changes. This will update files in the app and they need to commited. To migrate the data base run, `./manage.py migrate`.
