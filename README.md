# django

## Getting started

This project requires Python 3.x and NodeJs 8.x or better.

* Clone
* The setup script will set everything up and install all the dependencies
`source setup`. You should run this when ever you open a terminal to
work on this project.

## Running the project

To start the development server run `devserver`. This will start Django and
Webpack

## Updating the database

When a model is changed the databse needs to be migrated. To do this run
`./manage.py makemigrations` to stage the changes. This will update files in
the app and they need to commited. To migrate the data base run,
`./manage.py migrate`.

## Plugins

### DRF

We are using the Django Rest framwork to set up the RESR API:

https://www.django-rest-framework.org/

### Django-REST-Registration

User registration REST API, based on django-rest-framework.

https://github.com/apragacz/django-rest-registration

