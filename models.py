from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func 
#from flask_migrate import Migrate
import uuid
from datetime import datetime
from marshmallow import Schema, fields
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
import secrets


#set variables for class instantiation



ma = Marshmallow()
db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key = True, unique=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default= '')
    g_auth_verify = db.Column (db.Boolean, default = False)
    token = db.Column(db.String, default='', unique = True)
    date_created = db.Column(db.DateTime, nullable=False, server_default=func.now())



#every class has to have an init, all the things without a default must go to the front
    def __init__(self, email, first_name='', last_name='',password='', token='', g_auth_verify=False ):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    #now we will write the funtions for set_id, set_password, and set_token
    def set_token(self, length):
        return secrets.token_hex(length)   #this creates a unique token
        
    def set_id(self):
        return secrets.token_urlsafe()
        return str(uuid.uuid4()) #this generates a unique user id
        
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
        
    def __repr__ (self):
        return f'User{self.email} has been added to the database.'
        

        #now we need to make a class for the entries into the phonebook
class Contact(db.Model):
    id=db.Column(db.String, primary_key = True)
    name = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150))
    phone_number = db.Column(db.String(20))
    address=db.Column(db.String(200))
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__ ( self, name, email, phone_number, address, user_token, id=''):
        self.id = self.set_id()
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.user_token = user_token

    def __repr__(self):
        return f'The following person has been added to your phonebook: {self.name}'
        
    def set_id(self):
        return secrets.token_urlsafe()
        
class ContactSchema(ma.Schema):  #this is telling the app what happens when a new contact is made
    class Meta:
        fields = ['id', 'name', 'email', 'phone_number', 'address']

contact_schema = ContactSchema() #for one new contact
contacts_schema = ContactSchema(many=True) #for several new contacts

