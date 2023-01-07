import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from .database.models import db_drop_and_create_all, db_migrate, setup_db, Hike
from .auth.auth import AuthError, requires_auth
from config import app
from constants import HIKES_PER_PAGE

db_migrate(app)
setup_db(app)
CORS(app)


def paginate_hikes(request, data):
    page = request.args.get("page", 1, type=int)

    start = (page - 1) * HIKES_PER_PAGE
    end = start + HIKES_PER_PAGE

    hikes = [hike.short() for hike in data]
    current_hikes = hikes[start:end]

    return current_hikes

def paginate_detailed_hikes(request, data):
    page = request.args.get("page", 1, type=int)

    start = (page - 1) * HIKES_PER_PAGE
    end = start + HIKES_PER_PAGE

    hikes = [hike.long() for hike in data]
    current_hikes = hikes[start:end]

    return current_hikes

#Implement CORS
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Autorization, true")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, PUT, OPTIONS") 
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
# with app.app_context():
#     db_drop_and_create_all()

# ROUTES

'''
@TODO implement endpoint
    GET /hikes
'''

@app.route('/hikes')
def get_hikes():

    try:
        data = Hike.query.all()
        hikes = paginate_hikes(request, data)
        return jsonify({
            "success": True,
            "hikes": hikes
        })

    except:
        abort(404)


'''
@TODO implement endpoint
    GET /hikes-detail

'''
@app.route('/hikes-detail')
@requires_auth('get:hikes-detail')
def get_hikes_detail(payload):

    try:
        data = Hike.query.all()
        hikes = [hike.long() for hike in data]
        return jsonify({
            "success": True,
            "hikes": hikes
        })
    except:
        abort(404)

'''
@TODO implement endpoint
    POST /hikes
'''

@app.route('/hikes', methods=['POST'])
@requires_auth('post:hikes')
def create_hikes(payload):

    body = request.get_json()
    title = body.get('title')
    recipe = body.get('recipe')

    try:
        hike = Hike(title=title, recipe=json.dumps(recipe))
        hike.insert()
        return jsonify({
            "success": True,
            "hikes": hike.long()
        })

    except:
        abort(422)



'''
@TODO implement endpoint
    PATCH /hikes/<id>
'''

@app.route('/hikes/<int:hike_id>', methods=['PATCH'])
@requires_auth('patch:hikes')
def update_hike(hike_id, payload):

    if hike_id is None:
        abort(404)

    body = request.get_json()
    new_title = body.get('title')
    new_recipe = json.dumps(body.get('recipe'))

    try:
        hike = Hike.query.filter(Hike.id == hike_id).one_or_none()

        hike.title = new_title
        hike.recipe = new_recipe
        hike.update()
        return jsonify({
            "success" : True,
            "hike": hike.long()
        })
    except:
        abort(422)


'''
@TODO implement endpoint
    DELETE /hikes/<id>
'''

@app.route('/hikes/<int:hike_id>', methods=['DELETE'])
@requires_auth('delete:hikes')
def delete_drink(payload, hike_id):
    drink = Hike.query.filter(Hike.id == hike_id).one_or_none()

    if not drink:
        abort(404)
    
    try:
        drink.delete()
        return jsonify({
            "sucess": True
        })
    except:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
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

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
