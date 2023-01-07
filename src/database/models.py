import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_filename = "DB_FILE"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "postgresql:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def db_migrate(app):
    migrate = Migrate(app, db)

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # Demo row for POSTMAN test
    hike = Hike(
        title='SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED',
        price = 1500,
        description = "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!" ,
        duration = "5 Hours", # In Hours/days
        departs_from = "N°93 cité 261, Hai En nedjma, Oran",
        difficulty = 'Easy', # Array [Easy, Medium, Difficult] 
        group_max = 10,
        group_min = 5,
        min_age = '16',
        pick_up = True
    )

    hike.insert()

class Hike(db.Model):
    __tablename__ = "hikes"
    ##/* Examples: 
    # Title: SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED
    # Price : $159 / Adult
    # Description: ABOUT TIPT
    # AVAILABILITY  SEPT - APR
    # DURATION ~4 HOURS
    # DEPARTS FROM: Oran
    # DIFFICULTY: EASY [Easy, Medium, Difficult]
    # GROUP MAXIMUM: 15
    # MINIMUM AGE: 6 YEARS
    # PICK UP: YES
    # MEET ON LOCATION: NO
    # */

    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True) 
    price = db.Column(db.Double(), nullable=True)
    description = db.Column(db.String(500), nullable=True) 
    duration = db.Column(db.String(100), nullable=True) # In Hours/days
    departs_from = db.Column(db.String(255), nullable=True)
    difficulty = db.Column(db.String(255), nullable=True) # Array [Easy, Medium, Difficult] 
    group_max = db.Column(db.Integer, nullable=True)
    group_min = db.Column(db.Integer, nullable=True)
    min_age = db.Column(db.String(100), nullable=True)
    pick_up = db.Column(db.Boolean, default=False)
    available = db.Column(db.Boolean, default=True)
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self)

# class Review(db.Model):
#     __tablename__ = "reviews"
#     id = db.Column(db.Integer, primary_key=True)
#     stars = db.Column(db.Integer, nullable=False, default=1)
#     text = db.Column(db.String(500), nullable=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()

#     def __repr__(self):
#         return json.dumps(self)

class User(db.Model):
    __tablename__ = "users"

    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False) 
    id_number = db.Column(db.String(500), nullable=False) # MUST ME NOT NULLABLE
    birthday = db.Column(db.DateTime, nullable=False)
    # reviews = db.relationship('Review', backref='user', lazy=True)
    trips = db.relationship('Trip', backref='user', lazy=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self)

class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    booking_date = db.Column(db.DateTime, nullable=False)
    hike_id = db.Column(db.Integer, db.ForeignKey('hikes.id'), nullable=False)


    # def short(self):
    #     short_recipe = [{'color': r['color'], 'parts': r['parts']} for r in json.loads(self.recipe)]
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'recipe': short_recipe
    #     }

    # def long(self):
    #     return {
    #         'id': self.id,
    #         'title': self.title,
    #         'recipe': json.loads(self.recipe)
    #     }



    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self)
