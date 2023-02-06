#Create Virtual environment
py -3 -m venv venv

#activate environment
venv\scripts\activate

#Install requirements
pip install -r requirements.txt

#Run app
flask run

### `App Overview`
app = > this is entry point of app
main = > this folder contains all models, controllers and services
models = > added models for folder and notes table
controller = > added routes for folder and notes
services = > service related to controllers
utils => defined DTOs for Tables 