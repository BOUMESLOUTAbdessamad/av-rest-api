import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = 'adventure'
database_path = 'postgresql://{}/{}'.format('postgres:123456@localhost:5432', database_name)

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

    # Demo row for test
    hike = Hike(
        title='SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED',
        price = 1500,
        description = "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!" ,
        duration = "5 Hours", # In Hours/days
        departs_from = "N°93 cité 261, Hai En nedjma, Oran",
        difficulty = 'Easy', # Enum [Easy, Medium, Difficult] 
        group_max = 10,
        group_min = 5,
        min_age = '16',
        pick_up = True 
        # cover_image = "<IMAGE_URL>"
    )

    hike.insert()

class Hike(db.Model):
    __tablename__ = "hikes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True) 
    price = db.Column(db.Float, nullable=True)
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

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'price': self.price,
            'description': self.description,
            'duration': self.duration,
            'departs_from': self.departs_from,
            'difficulty': self.difficulty,
            'group_max': self.group_max,
            'group_min': self.group_min,
            'min_age': self.min_age,
            'pick_up': self.pick_up,
            'available': self.available,
            }
    
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
    name = db.Column(db.String(255), nullable=False) 
    id_number = db.Column(db.String(500), nullable=False) # MUST BE NOT NULLABLE
    birthday = db.Column(db.DateTime, nullable=False)
    # reviews = db.relationship('Review', backref='user', lazy=True)
    trips = db.relationship('Trip', backref='user', lazy=True)
    created_at=db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_verified = db.Column(db.String(255),default=False, nullable=False)
    family_name= db.Column(db.String(255), nullable=False)
    given_name= db.Column(db.String(255), nullable=False)
    identities = db.Column(db.String(255), nullable=False)
    locale = db.Column(db.String(4), nullable=False)
    # name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.String(255), nullable=False, unique=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

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
