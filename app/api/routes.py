from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, Contact, User, contact_schema, contacts_schema
# from models import db, User, contact_schema, contacts_schema

api = Blueprint('api', __name__, url_prefix='/api') #prefix means that it goes before the slug

@api.route('/getdata')
def getdata():
    return {'Yee': 'haaawww'}

@api.route('/contacts', methods = ['POST'])
@token_required
def create_contact(current_user_token):
    name = request.json['name']
    email = request.json['email']
    phone_number = request.json['phone_number']
    address = request.json['address']
    user_token = current_user_token

    print(f'BIG TESTER: {current_user_token.token}')

    contact = Contact(name, email, phone_number, address, user_token=user_token) #we do user_token = user_toked to over-write
    #the previous value for that variable

    db.session.add(contact)
    db.session.commit()

    response = contact_schema.dump(contact)
    return jsonify(response)

##NOW WE ARE GOING TO DO SOMTHING DIFFERENT,,,, GET not POST

@api.route('/contacts', methods = ['GET'])
@token_required

def get_contact(current_user_token):
    a_user = current_user_token.token
    contacts = Contact.query.filter_by(user_token = a_user).all()
    response = contacts_schema.dump(contacts)
    return jsonify(response)