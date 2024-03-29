
from sqlalchemy import Column, String, Integer

import json


from database.hike_models import Hike, Category
from server_config import db


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    # Demo row for test
    hike = Hike(
        title='SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED',
        price = 1500,
        description = "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!" ,
        duration = "5 Hours", # In Hours
        departs_from = "Oran",
        difficulty = 'Easy', # Enum [Easy, Medium, Difficult]
        distance = 10.5, # 10.5 KM
        group_max = 10,
        group_min = 5,
        min_age = '16',
        pick_up = True 
    )
    hike.insert()

def db_create_all():
    db.create_all()
    
    # Demo row for test
    hike = Hike(
        title='SUPER JEEP NORTHERN LIGHTS HUNT - FREE PHOTOS INCLUDED',
        price = 1500,
        description = "On this super jeep excursion, we take you off the beaten track and chase one of the world's most mysterious phenomena. Leave the city's bright lights behind to see the Northern Lights while your guide tells you about this natural wonder!" ,
        duration = "5 Hours", # In Hours
        departs_from = "N°93 cité 261, Hai En nedjma, Oran",
        # depart_date = "12-06-2023"
        difficulty = 'Easy', # Enum [Easy, Medium, Difficult]
        distance = 10.5, # 10.5 KM
        group_max = 10,
        group_min = 5,
        min_age = '16',
        pick_up = True 
    )

    hike.insert()



class User(db.Model):
    __tablename__ = "users"

    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False) 
    id_number = db.Column(db.String(500), nullable=False) # MUST BE NOT NULLABLE
    birthday = db.Column(db.DateTime, nullable=False)
    # reviews = db.relationship('Review', backref='user', lazy=True)
    created_at=db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_verified = db.Column(db.String(255),default=False, nullable=False)
    family_name= db.Column(db.String(255), nullable=False)
    given_name= db.Column(db.String(255), nullable=False)
    identities = db.Column(db.String(255), nullable=False)
    locale = db.Column(db.String(4), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.String(255), nullable=False, unique=True)
    trips = db.relationship('Trip', backref='user', lazy=True)

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
            'name': self.name,
            'id_number': self.id_number,
            'birthday': self.birthday,
            'created_at': self.created_at,
            'email': self.email,
            'email_verified': self.email_verified,
            'family_name': self.family_name,
            'given_name': self.given_name,
            'identities': self.identities,
            'locale': self.locale,
            'nickname': self.nickname,
            'picture': self.picture,
            'user_id': self.user_id,
            }

    def __repr__(self):
        return json.dumps(self)

class Trip(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    booking_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), default="ordered",  nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    hike_id = db.Column(db.Integer, db.ForeignKey('hikes.id'), nullable=False)
    auth0_user_id = db.Column(db.String(), nullable=True)

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

    def format(self):
        return {
            "id": self.id,
            "booking_date": self.booking_date,
            "user_id": self.user_id,
            "hike_id": self.hike_id,
            "auth0_user_id": self.auth0_user_id,
            "status": self.status,
        }

    def format_trips_by_user(self):

        return {
            "id": self.id,
            "booking_date": self.booking_date,
            "user_id": self.user_id,
            "hike_id": self.hike_id,
            'title': self.hike.title,
            'price': self.hike.price,
            'description': self.hike.description,
            'duration': self.hike.duration,
            'departs_from': self.hike.departs_from,
            'difficulty': self.hike.difficulty,
            'group_max': self.hike.group_max,
            'group_min': self.hike.group_min,
            'min_age': self.hike.min_age,
            'pick_up': self.hike.pick_up,
            'available': self.hike.available,
        }