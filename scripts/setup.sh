#!/usr/bin/env bash

./scripts/subMudInit.sh

if [ ! -d ./env ]; then
	printf "\nVirtual environment not found, creating it\n"
	sleep 1
	virtualenv env -p python3
fi

printf "\nActivating virtual environment...\n"
source env/bin/activate

printf "\n\nInstalling python packages..\n\n"
pip install -r backend/requirements.txt

if [ -d ./frontend ]; then
	printf "\n\nInstalling Node packages...\n\n"
	npm --prefix ./frontend/ install ./frontend/
	
	printf "\nAdding nodeJS modules bin to your path\n\n"
	export PATH=`pwd`/frontend/node_modules/.bin/:$PATH
fi

printf "\nAdding scripts folder to your path\n\n"
export PATH=`pwd`/scripts/:$PATH

printf "\n\nSetting up environment alias\n"
