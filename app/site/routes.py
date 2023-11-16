from flask import Blueprint, render_template 

#this code below does the same as the code on __init__. site means idk, but __name__ is connecting it to a cloud 
# of information somehow, it has somthing to do with flask, then template_folder = site_templates is making a variable 
#with our index.html and profile.html from our site foulder and site_template path.
site = Blueprint ('site', __name__, template_folder='site_templates')
#we call it site instead of 'app' to keep things seperate. that way if there is an issue, we can find the source and 
#and we look through less code to find the error. instead of looking through 1000 lines of code. we will 
#connect everything later.


@site.route('/')
def home():      #like before, we make a pathway through a server to out index.html using the render_template function in flask
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template ('profile.html')