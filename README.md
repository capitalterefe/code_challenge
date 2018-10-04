# Find Largest word in a file and Transpose

This project is a python based utility that implements finding largest word
from a file and Transpose, Not enough but few test scenarios are included
to make the utility reliable.

- A sample data file is included for testing purpose

## Table of Contents

- [Read this first](#read-this-first)
- [Installation](#installation)
- [Usage](#usage)

## Read this first

- If you believe you found a bug with how this utility behaves in your environment,
  please make sure you are running on python3.


## installation

download python3 from https://www.python.org/

update you python path
```
>vi .bash_profile
>PATH="/Library/Frameworks/Python.framework/Versions/{version}/bin:${PATH}"
>export PATH
```

pip install virtualenv (Optional)
```
>sudo virtualenv -p python3 <targetFolder>
>souce <targetFolder>/bin/activate
```
Pipenv automatically creates and manages a virtualenv for your projects
```
>sudo pip install pipenv
>change the permission to 777 /Users/ct/.local/share/virtualenvs to avoid typing sudo
>chmod 777 virtualenvs
```

## Usage

change your directory to project directory
```
> cd CODING_CHALLENGE/tests \n
```
Export your modules to the python path
```
> export PYTHONPATH=$PYTHONPATH:/<path_to_modules>
```
 Run with python3
```
> python3 test_find_largest_word.py
```
