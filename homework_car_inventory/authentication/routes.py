from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/mygarage')
def my_garage():
    return render_template('mygarage.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signin')
def signin():
    return render_template('signin.html')