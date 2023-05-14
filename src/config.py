import os
from flask import Flask
from database.models import db_migrate, setup_db
from flask_cors import CORS
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.

basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

#Create the app
app = Flask(__name__)
app.secret_key = SECRET_KEY


# DONE IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/safarinetwork'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

AUTH0_DOMAIN = 'dev-aib6p7npbv32c4ov.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'https://127.0.0.1:5000/'


db_migrate(app)
setup_db(app)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Autorization, true")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, PUT, OPTIONS") 
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response