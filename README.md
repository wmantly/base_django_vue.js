# {unnamed project}

## Getting started

This project requires Python 3.x, `virtualenv` and NodeJs 8.x or better.

Node and `virtualenv` are development dependencies and are not need for
production.

* Clone
* The setup script will set everything up and install all the dependencies
`source scripts/setup.sh`. **THIS MUST BE EXECUTED FROM THE ROOT OF THE PROJECT** You should run this when ever you open a terminal to
work on this project.

## Running the project

To start the development server run `devserver`. This will start Django and
Webpack

## Directory structurer

### `env/`

This is the virtual environment directory for the python aspect of this project.
It is not tracked and unique to each computer. Its is also not movable. There
is no reason to interact with this directory directly.

### `backend/`

This directory hold the Django projecy. `manage.py` is set to be part of your
path when you activate the development environment and you do not have to worry
about where it is being executed from. Also, **DO NOT** pre-pend `manage.py`
with `python/3` or `./`, this will break stuff.

All the Django apps and config are also kept in this directory.

The `requirements.txt` file is also kept here.

### `frontend/`

This is where the Vue.JS project and any front end or static resources are kept.

The `package.json` file is also here.

When the development environment is activated, the
`/frontend/node_modules/.bin/` directory is pre-pended to your path.

### `scripts/`

This directory holds scripts for helping with the development process.

When the development environment is activated, the `scripts` directory is
pre-pended to your path.

## Updating the database

When a model is changed the databse needs to be migrated. To do this run
`manage.py makemigrations` to stage the changes. This will update files in
the app and they need to commited. To migrate the data base run,
`manage.py migrate`.

## API documents

This project uses self documenting tools for API references. They can be found
at while they server is running:

http(s)://{site URL}/api/swagger/

http(s)://{site URL}/api/redoc/


## Plugins

### Django Rest framwork

We are using the Django Rest framwork to set up the RESR API:

https://www.django-rest-framework.org/

### Django-REST-Registration

User registration REST API, based on django-rest-framework.

https://github.com/apragacz/django-rest-registration

### drf-yasg - Yet another Swagger generator

Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework
API.

https://github.com/axnsan12/drf-yasg/
