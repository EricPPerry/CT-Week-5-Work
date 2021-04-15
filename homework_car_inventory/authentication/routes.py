from flask import Blueprint, render_template, request, flash, redirect, url_for
from homework_car_inventory.forms import UserLoginForm
from homework_car_inventory.models import User, db, check_password_hash
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/mygarage')
@login_required
def my_garage():
    return render_template('mygarage.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            first_name = form.first_name.data
            last_name = form.last_name.data

            print(email,password, first_name, last_name)

            user = User(email, password = password, first_name = first_name, last_name = last_name)
            
            db.session.add(user)
            db.session.commit()
            flash(f'You have successfully created a user account for {email}!!!! Welcome!', 'user-created')

            return redirect(url_for('main_site.home'))
    
    except:
        raise Exception('Sorry, Invalid Form Data: Please Check Your FOrm Inputs!!!')
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = UserLoginForm()

    #try to get info and validate the form, if it isnt found - give error
    try:
        #checks if the request from form submission is set to 'POST' and form is validated
        if request.method == 'POST' and form.validate_on_submit():
            #set variables equal to values entered into signin form
            email = form.email.data
            password = form.password.data
            #print lets us know these things are getting pulled correctly, helps error checking/finding
            print(email,password)

            #we want to filter by the email provided by the form (defined above)
            #.first() asks for first value that comes back under this query
            logged_user = User.query.filter(User.email == email).first()

            #want to check password and currently logged user
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully logged in: via email/password', 'auth-success')
                return redirect(url_for('main_site.home'))
            else:
                flash('Your email/password is incorrect', 'auth-failed')
                return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form!')
    
    #pass the form = UserLoginForm() to return statement
    return render_template('signin.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_site.home'))