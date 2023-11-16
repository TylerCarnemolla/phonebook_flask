from forms import UserLoginForm

from models import User, db, check_password_hash

from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, LoginManager, current_user, login_required

auth = Blueprint('auth', __name__, template_folder = 'auth_templates') #template folder is linked to where people will unput 
                        #user name and stull

@auth.route('/signup', methods = ['GET', 'POST']) #at this /signup location, these mothods will be used

#when at /signup.. do this function
def signup():
    form = UserLoginForm()   #this is a class we made forms.py

    try:   #post means that a user POSTS information, aka submits a username or somthing
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data 
            print(email, password)#if the inputed email and pass are == to the standards of the tools at forms.py
                                            #do somthing
            user = User(email, password = password) #user = the user class made in models.py and the password passed in
            # is stored 

            db.session.add(user) #this adds the data to the db
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'User-created')
            return redirect(url_for('site.home')) #redirect takes you back to the given location.. site.home on routes.py
    except:
        raise Exception('Invalid form data: Please check your form.')
    return render_template('sign_up.html', form=form) #this recycles the page so they can try again

#now for the sign-in page

@auth.route('/signin', methods = ['GET', 'POST'])

def signin():
    form = UserLoginForm()

    try:   #post means that a user POSTS information, aka submits a username or somthing
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data 
            print(email, password)#if the inputed email and pass are == to the standards of the t
            
            logged_user = User.query.filter(User.email == email).first() #logged user = the first person with the right
                                                                            #email that is in our db
            if logged_user and check_password_hash(logged_user.password, password):#if logged=user exists, and the 
                #passowrd is de=hashed and accurate, 
                login_user(logged_user)
                flash('You successfully signed in.')
                return redirect(url_for('site.profile'))
            else:
                flash(f"You have failed to get in, you shall not paaaaasssss.")
    except:
        raise Exception ('Somthing went wrong, please check your sign in information')
    return render_template('sign_in.html', form = form)
            

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))