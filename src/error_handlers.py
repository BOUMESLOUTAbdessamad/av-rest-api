
from auth.auth import AuthError
from flask import jsonify
from config import app




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
