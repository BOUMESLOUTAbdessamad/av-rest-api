import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

from server_config import db


class Hike(db.Model):
    __tablename__ = "hikes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=True) 
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.String(500), nullable=True) 
    duration = db.Column(db.String(100), nullable=True) # In Hours
    departs_from = db.Column(db.String(255), nullable=True)
    depart_date = db.Column(db.DateTime, nullable=True)
    difficulty = db.Column(db.String(255), nullable=True) # Array [Easy, Medium, Difficult] 
    distance = db.Column(db.Float, nullable=True)
    group_max = db.Column(db.Integer, nullable=True)
    group_min = db.Column(db.Integer, nullable=True)
    min_age = db.Column(db.String(100), nullable=True)
    pick_up = db.Column(db.Boolean, default=False)
    available = db.Column(db.Boolean, default=True)
    trips = db.relationship('Trip', backref='hike')
    categories = db.relationship('Category', backref='hike') # Treck, Camping, Bushcraft, Short Stay, Trend
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    cover = db.Column(db.String(), nullable=True)
    
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
            'distance': self.distance,
            'departs_from': self.departs_from,
            'difficulty': self.difficulty,
            'depart_date': self.depart_date,
            'group_max': self.group_max,
            'group_min': self.group_min,
            'min_age': self.min_age,
            'pick_up': self.pick_up,
            'available': self.available,
            'cover' : self.cover
            }
    
    def __repr__(self):
        return json.dumps(self)
    
class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=True) 
    description = db.Column(db.String(500), nullable=True) 
    cover = db.Column(db.String(), nullable=True)
    hikes = db.relationship('Hike', backref='category')

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
            'description': self.description,
            'cover': self.cover,
            }
    
    def __repr__(self):
        return json.dumps(self)