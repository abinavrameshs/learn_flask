# Flask-RESTful and Authentication

We use venv module in python to create a virtual environment, then use Flas-Restful package to built REST-ful APIs

# USeful commands

`pip freeze` : Will list all libraries installed
`pip install virtualenv` : Will install the package 'virtualenv' that helps in creating virtual environment

`virtualenv venv` : Will utilize the virualenv package to create a virtual environment with latest version of python. This step will create a folder within the current directory called "venv", with python installed. Then run

`venv\Scripts\activate.bat` : We run this command to run the .bat file under venv/Scripts. This will activate the virtual environment created. This command can be run on windows. for mac or linux, we need to run source command.

`deactivate` : to come out of the virtual environment

`pip install Flask-RESTful` : Will install Flask-RESTful package within the virtual env

1. app.py : Runs for a student resource
2. app_items.py : Runs for item and itemlist resource

## For Authentication and security : 

1. Install  `Flask-JWT` by doing `pip install Flask-JWT`
2. go to 'with_security' folder and run "app_items_security.py"
- Need to authenticate using /auth POST API ==> This will give an access token
- wherever we havve the decorator `@jwt_required()`, we need to use those APIs along with `Authorization= JWT <auth_id>` to run the corresponding API