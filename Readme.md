#Create Virtual environment
py -3 -m venv venv

#activate environment
venv\scripts\activate

#Install requirements
pip install -r requirements.txt

#Run app
flask run