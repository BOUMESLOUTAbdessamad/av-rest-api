from flask_sqlalchemy import SQLAlchemy
from config import app
from flask_migrate import Migrate


db = SQLAlchemy(app)
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


