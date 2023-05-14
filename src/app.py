import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json

from database.models import db_drop_and_create_all, db_create_all,  db_migrate, setup_db, Hike, User, Trip
from auth.auth import AuthError, requires_auth
from config import app
from constants import RECORDS_PER_PAGE
from datetime import datetime
from helpers import paginate_hikes

#CODE in a spcecific date git commit --date="2023-03-00 00:00:00"

# with app.app_context():
#     db_create_all()

# with app.app_context():
#     db_drop_and_create_all()


# ROUTES
@app.route('/') # GET /api/v0/hikes
def index():
    return "Welcome to Adventure Vibe"

##Hikes

@app.route('/api/v0/hikes') # GET /api/v0/hikes
def get_hikes():
    data = Hike.query.all()
    hikes = paginate_hikes(request, data)
    try:

        return jsonify({
            "success": True,
            "hikes": hikes
        })

    except:
        abort(404)

@app.route('/api/v0/hikes-detail/<int:hike_id>') # GET /api/v0/hikes-detail/<int:hike_id>
def get_hikes_detail(hike_id):

    try:
        data = Hike.query.filter(Hike.id==hike_id).one_or_none()

        return jsonify({
            "success": True,
            "hike": data.format()
        })
    except:
        abort(404)


@app.route('/api/v0/hikes', methods=['POST']) # POST /api/v0/hikes
@requires_auth('post:hikes')
def create_hikes(payload):

    body = request.get_json()
    title = body.get('title')
    price = body.get('price')
    description = body.get('description')
    duration = body.get('duration')
    departs_from = body.get('departs_from') # Google Maps API
    difficulty = body.get('difficulty')
    group_max = body.get('group_max')
    group_min = body.get('group_min')
    min_age = body.get('min_age')
    pick_up = body.get('pick_up')


    try:
        hike = Hike(
                title=title,
                price=price,
                description=description,
                duration=duration,
                departs_from=departs_from,
                difficulty=difficulty,
                group_max=group_max,
                group_min=group_min,
                min_age=min_age,
                pick_up=pick_up
            )
        
        hike.insert()
        return jsonify({
            "success": True,
            "hikes": hike.format()
        })

    except:
        abort(422)


@app.route('/api/v0/hikes/<int:hike_id>', methods=['PATCH']) # PATCH /api/v0/hikes/<int:hike_id>
@requires_auth('patch:hikes')
def update_hike(payload, hike_id):

    if hike_id is None:
        abort(404)

    body = request.get_json()
    title = body.get('title')
    price = body.get('price')
    description = body.get('description')
    duration = body.get('duration')
    departs_from = body.get('departs_from')
    difficulty = body.get('difficulty')
    group_max = body.get('group_max')
    group_min = body.get('group_min')
    min_age = body.get('min_age')
    pick_up = body.get('pick_up')
    # cover_image = body.get('cover_image')

    try:
        hike = Hike.query.filter(Hike.id == hike_id).one_or_none()

        hike.title = title
        hike.price = price
        hike.description = description
        hike.duration = duration
        hike.departs_from = departs_from
        hike.difficulty = difficulty
        hike.group_max = group_max
        hike.group_min = group_min
        hike.min_age = min_age
        hike.pick_up = pick_up

        hike.update()

        return jsonify({
            "success" : True,
            "hike": hike.format()
        })
    except:
        abort(422)


@app.route('/api/v0/hikes/<int:hike_id>', methods=['DELETE']) # DELETE /api/v0/hikes/<int:hike_id>
@requires_auth('delete:hikes')
def delete_drink(payload, hike_id):
    hile = Hike.query.filter(Hike.id == hike_id).one_or_none()

    if not hile:
        abort(404)
    
    try:
        hile.delete()
        return jsonify({
            "sucess": True,
            "message": "Hike deleted!"
        })
    except:
        abort(422)

##Users

@app.route('/api/v0/users')
@requires_auth('get:users')
def get_users(payload):
    data = User.query.all()
    users = paginate_hikes(request, data)
    try:
        return jsonify({
            "success": True,
            "users": users
        })

    except:
        abort(404)


@app.route('/api/v0/users', methods=['POST'])
@requires_auth('post:users')
def add_user(payload):

    body = request.get_json()

    id_number = body.get('id_number')
    name = body.get('name')
    user_id = body.get('user_id')
    picture = body.get('picture')
    nickname = body.get('nickname')
    locale = body.get('locale')
    identities = json.dumps(body.get('identities'))
    given_name = body.get('given_name')
    family_name = body.get('family_name')
    email_verified = body.get('email_verified')
    email = body.get('email')
    birthday = body.get('birthday')
    created_at = datetime.now()

    try:
        user = User(
            id_number =id_number,
            name = name,
            user_id = user_id,
            picture = picture,
            nickname = nickname,
            locale = locale,
            identities = identities,
            given_name = given_name,
            family_name = family_name,
            email_verified = email_verified,
            email = email,
            birthday = birthday,
            created_at = created_at,
            # updated_at = updated_at
        )

        user.insert()
        return jsonify({
            "user": user.format()
        })
    except:
        abort(422)


@app.route('/api/v0/user-details')
@requires_auth('get:user-details')
def user_details(payload):

    return jsonify({
        "success": True,
        "user-payload": payload
    })


#Get all trips
@app.route('/api/v0/trips')
@requires_auth('get:trips')
def get_bookings(payload):

    try:
        data = Trip.query.all()
        trips = [trip.format() for trip in data]
        return jsonify({"trips": trips})
    except:
        abort(404)

#Add trips
@app.route('/api/v0/trips', methods = ['POST'])
@requires_auth('post:trips')
def book_hike(payload):

    body = request.get_json()
    hike_id = body.get('hike_id')
    auth0_user_id = payload.get('sub') # Get user_id from auth0 token
    hike = Hike.query.filter(Hike.id == hike_id).one_or_none() # Get the user_id from the current auth0 session

    try:
        trip = Trip(booking_date=datetime.now(), hike=hike, auth0_user_id=auth0_user_id)
        trip.insert()
        return jsonify({"trip": trip.format()})
    except:
        abort(422)


# Get Trips by user
@app.route('/api/v0/users/<user_id>/trips')
@requires_auth('get:user-trips')
def get_trips_by_user(payload, user_id):

    trips = Trip.query.join(Hike).filter(Trip.auth0_user_id == user_id).all()

    return jsonify({
        "success": True,
        "trips": [trip.format_trips_by_user() for trip in trips],
    })



# DELETE Trip
@app.route('/api/v0/users/<user_id>/trips/<trip_id>', methods=['DELETE'])
# @requires_auth('delete:user-trips')
def delete_trip_by_user(payload, user_id, trip_id):

    trip = Trip.query.filter(Trip.auth0_user_id == user_id, Trip.id == trip_id).one_or_none()

    try:
        trip.delete()
        return jsonify({
            "success": True,
            "message": "Trip deleted"
        })
    except:
        abort(422)



