
from functools import wraps
import secrets
from flask import request, jsonify, json
import decimal
import json as json_module
from models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'message':'Token is missing'}), 401
        
        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(token)
            print(current_user_token)

        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify ({'message': 'Token is invalid'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated


class JSONEncoder(json_module.JSONEncoder):
    def default(self, obj):     #this checks an object from a class to see if it is a particular type
        if isinstance(obj, decimal.Decimal): #if it is a deciaml
            return str(obj) #return it as a string
        return super(JSONEncoder, self).default(obj)