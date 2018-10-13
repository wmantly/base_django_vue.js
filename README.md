# django

## Getting started

This project requires Python 3.x, `virtualenv` and NodeJs 8.x or better.

Node and `virtualenv` are development dependencies and are not need for
production.

* Clone
* The setup script will set everything up and install all the dependencies
`source setup`. You should run this when ever you open a terminal to
work on this project.

## Running the project

To start the development server run `devserver`. This will start Django and
Webpack

## Directory structurer

### `backend/`

This directory hold the Django projecy. `manage.py` is set to be part of your
path when you activate the development environment and you do not have to worry
about where is being executed from. Also, **DO NOT** pre-pend `manage.py` with
`python/3` or `./`, this will break stuff.

All the Django apps and config are also kept in this directory.

The `requirements.txt` file is also kept here.

### `frontend/`

This is where the Vue.JS project and any front end or static resources are kept.

The `package.json` file is also here.

When the development environment is activated, the `/frontend/node_modules/.bin/`
directory is pre-pended to you path.

### `scripts/`

This directory holds scripts for helping with the development process. When the
development environment is activated, the `scripts` directory is pre-pended to
you path.

## Updating the database

When a model is changed the databse needs to be migrated. To do this run
`manage.py makemigrations` to stage the changes. This will update files in
the app and they need to commited. To migrate the data base run,
`manage.py migrate`.

## Plugins

### DRF

We are using the Django Rest framwork to set up the RESR API:

https://www.django-rest-framework.org/

### Django-REST-Registration

User registration REST API, based on django-rest-framework.

https://github.com/apragacz/django-rest-registration
