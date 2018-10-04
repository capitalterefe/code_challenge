# Find Largest word in the file And Transpose

This project is a python based utility that implements finding largest word
from a file and Transpose, Not enough but sample test scenarios are included
to make the utility reliable.

## Table of Contents

- [Read this first](#read-this-first)
- [Installation](#installation)
- [Usage](#usage)

## Read this first

- If you believe you found a bug with how this utility behaves in your environment,
  please make sure you are first have python3 is installed in your machine.
- A sample data file is included for testing purpose

#installation

download python from https://www.python.org/
vi .bash_profile
PATH="/Library/Frameworks/Python.framework/Versions/{version}/bin:${PATH}"
export PATH

pip install virtualenv
sudo virtualenv -p python3 <targetFolder>
souce <targetFolder>/bin/activate

Pipenv automatically creates and manages a virtualenv for your projects
sudo pip install pipenv
change the permission to 777 /Users/ct/.local/share/virtualenvs to avoid typing sudo
chmod 777 virtualenvs

## Usage

change your directory to project directory

> cd CODING_CHALLENGE/tests
> Export your modules to the python path
> export PYTHONPATH=$PYTHONPATH:/<path_to_modules>
> Run
> python3 test_find_largest_word.py
