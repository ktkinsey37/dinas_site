import os

from flask_wtf import FlaskForm
from flask import Flask, render_template, request, jsonify, flash, redirect, session, g
import random, requests
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime, timedelta
from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Item

app = Flask(__name__)

CURR_USER_KEY = "curr_user"

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///repnile').replace("://", "ql://", 1))

print(app.config['SQLALCHEMY_DATABASE_URI'])

google_api_key = os.environ.get('google_api_key', False)
api_key = os.environ.get('api_key', '2963e96aecde4c5093c215021211406')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

google_api = google_api_key
api_key = api_key
base_url = 'http://api.weatherapi.com/v1'


########################### USER ROUTES ############################
@app.before_request
def add_user_to_g():
    """If user is in session, retrieve them"""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Log out user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username or email already taken", 'danger')
            return render_template('signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    flash("Successfully logged out!")
    session.pop(CURR_USER_KEY)
    return redirect('/', code=302)

@app.route('/add_admin', methods=["GET", "POST"])
def add_admin():

    try:
        
        if g.user.authority == 'admin':


            form = AddAdmin()

                
            if form.validate_on_submit():

                print("FORM VALIDATED")

                
              
                new_admin = User.query.filter_by(username=form.data['name']).first()
                new_admin.authority = 'admin'


                db.session.add(new_admin)
                db.session.commit()

                return redirect('/', code=302)
            
            else:
                flash("There was an error processing the form.", 'danger')
                return render_template('add-admin.html', form=form)

        else:
            flash('You do not have the proper authority to visit this page.')
            return redirect('/', code=302)

    except (AttributeError):
        flash('There is no user currently signed in')
        return redirect('/', code=302)

@app.route("/")
def homepage():
    """Show homepage."""

    popular_locations=Location.query.filter_by(user_id=admin.id).limit(25).all()

    return render_template('home.html', popular_locations=popular_locations, form=form)