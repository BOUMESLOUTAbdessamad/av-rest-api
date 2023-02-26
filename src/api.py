import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from database.models import db_drop_and_create_all, db_migrate, setup_db, Hike, User, Trip
from auth.auth import AuthError, requires_auth
from config import app
from constants import HIKES_PER_PAGE
from datetime import datetime


db_migrate(app)
setup_db(app)
CORS(app)

def paginate_hikes(request, data):
    page = request.args.get("page", 1, type=int)

    start = (page - 1) * HIKES_PER_PAGE
    end = start + HIKES_PER_PAGE

    hikes = [hike.format() for hike in data]
    current_hikes = hikes[start:end]

    return current_hikes

#Implement CORS
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Autorization, true")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, PUT, OPTIONS") 
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


with app.app_context():
    db_create_all()

# ROUTES
@app.route('/api/v0/hikes')
def get_hikes():
    data = Hike.query.all()
    hikes = paginate_hikes(request, data)
    print(hikes)
    try:


        return jsonify({
            "success": True,
            "hikes": hikes
        })

    except:
        abort(404)

@app.route('/api/v0/hikes-detail/<int:hike_id>')
def get_hikes_detail(hike_id):

    try:
        data = Hike.query.filter(Hike.id==hike_id).one_or_none()

        return jsonify({
            "success": True,
            "hikes": data.format()
        })
    except:
        abort(404)


@app.route('/api/v0/hikes', methods=['POST'])
@requires_auth('post:hikes')
def create_hikes():

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


@app.route('/api/v0/hikes/<int:hike_id>', methods=['PATCH'])
# @requires_auth('patch:hikes')
def update_hike(hike_id):

    if hike_id is None:
        abort(404)

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
    # cover_image = body.get('cover_image')


    # new_recipe = json.dumps(body.get('recipe'))

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


@app.route('/api/v0/hikes/<int:hike_id>', methods=['DELETE'])
# @requires_auth('delete:hikes')
def delete_drink(hike_id):
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


#Users
@app.route('/api/v0/users')
def get_users():
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
def add_user():

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
    # updated_at = datetime.now()

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


#Users
# @app.route('/api/v0/logout')
# @requires_auth('get:user-details')
# def logout(payload):
#     data = User.query.all()
#     users = paginate_hikes(request, data)

#     try:
#         return jsonify({
#             "success": True,
#             "users": users
#         })

#     except:
#         abort(404)

@app.route('/api/v0/user-details')
@requires_auth('get:user-details')
def user_details(payload):

    return jsonify({
        "success": True,
        "user-payload": payload
    })
    
#Get all trips
@app.route('/api/v0/trips')
def get_bookins():
    data = Trip.query.all()
    trips = [trip.format() for trip in data]
    return jsonify({"trips": trips})

#Add trips
@app.route('/api/v0/trips', methods = ['POST'])
@requires_auth('post:trips')
def book_hike(payload):
    
    body = request.get_json()
    hike_id = body.get('hike_id')
    user_id = payload.get('sub') # Get user_id from auth0 token

    # print(user_id)
    hike = Hike.query.filter(Hike.id == hike_id).one_or_none() # Get the user_id from the current auth0 session
    user = User.query.filter(User.user_id == user_id).one_or_none() # Get the hike_id from the DB

    trip = Trip(booking_date=datetime.now(), user=user, hike=hike)
    
    trip.insert()
    return jsonify({"trip": trip.format()})


# Get Trips by user
@app.route('/api/v0/users/<user_id>/trips')
def get_trips_by_user(user_id):
    
    trips = Trip.query.join(Hike).filter(Trip.user_id == user_id).all()

    return jsonify({
        "success": True,
        "trips": [trip.format_trips_by_user() for trip in trips]
    })


# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "not found"
    }), 404

@app.errorhandler(401)
def unauthorised(error):
    return jsonify({
            "success": False, 
            "error": 401, 
            "message": "unauthorised"
    }), 401

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
            "success": False, 
            "error": 400, 
            "message": "bad request"
        }), 400

@app.errorhandler(AuthError)
def auth_error_handler(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

