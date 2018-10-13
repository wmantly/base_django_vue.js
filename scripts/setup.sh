#!/usr/bin/env bash

if [ ! -d ./env ]; then
	printf "Virtual environment not found, creating it\n"
	sleep 1
	virtualenv env -p python3
fi

printf "Activating virtual environment...\n"
source env/bin/activate

printf "\nInstalling python packages..\n"
pip install -r backend/requirements.txt

if [ -d ./frontend ]; then
	printf "\nInstalling Node packages...\n"
	npm --prefix ./frontend/ install ./frontend/
	
	printf "Adding nodeJS modules bin to your path\n"
	export PATH=`pwd`/frontend/node_modules/.bin/:$PATH
	export NODE_ENV="development"
fi

printf "Adding scripts folder to your path\n"
export PATH=`pwd`/scripts/:$PATH

printf "\nSetting up environment alias\n"
