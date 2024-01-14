import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database_name = 'adventure'

if os.getenv('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
else:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}/{}'.format('postgres:123456@localhost:5432', database_name)

db = SQLAlchemy()

def db_migrate(app):
    migrate = Migrate(app, db)

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)