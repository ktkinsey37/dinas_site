import os

from flask_wtf import FlaskForm
from flask import Flask, render_template, request, jsonify, flash, redirect, session, g
import random, requests
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime # timedelta
# from sqlalchemy.exc import IntegrityError
from models import db, connect_db, User, Item, Animal, Event

app = Flask(__name__)

CURR_USER_KEY = "curr_user"

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///repnile').replace("://", "ql://", 1))

print(app.config['SQLALCHEMY_DATABASE_URI'])

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

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

# @app.route('/add_admin', methods=["GET", "POST"])
# def add_admin():

#     try:
        
#         if g.user.authority == 'admin':


#             form = AddAdmin()

                
#             if form.validate_on_submit():

#                 print("FORM VALIDATED")

                
              
#                 new_admin = User.query.filter_by(username=form.data['name']).first()
#                 new_admin.authority = 'admin'


#                 db.session.add(new_admin)
#                 db.session.commit()

#                 return redirect('/', code=302)
            
#             else:
#                 flash("There was an error processing the form.", 'danger')
#                 return render_template('add-admin.html', form=form)

#         else:
#             flash('You do not have the proper authority to visit this page.')
#             return redirect('/', code=302)

#     except (AttributeError):
#         flash('There is no user currently signed in')
#         return redirect('/', code=302)

@app.route("/")
def homepage():
    """Show homepage."""

    # popular_locations=Location.query.filter_by(user_id=admin.id).limit(25).all()

    return render_template('home.html') # popular_locations=popular_locations, form=form)

########################### SHOP ITEM/ANIMAL ROUTES ############################

@app.route("/shop")
def shop_homepage():
    """Renders the shop's homepage."""

    items = Item.query.limit(25).all() #How do you want to filter the first items that come up?
    animals = Animal.query.limit(5).all()
    events = Event.query.all()
    
    return True

@app.route("/items")
def items_homepage():
    """Renders the shop's homepage."""

    items = Item.query.limit(25).all() #How do you want to filter the first items that come up?
    animals = Animal.query.limit(5).all()
    events = Event.query.all()
    
    return True

@app.route('/items/<item_id>')
def item(item_id):
    """Show a location and its details."""

    item = Item.query.get_or_404(item_id)

    return render_template('location-view.html', item=item)

@app.route('/animals')
def animals_homepage():

    animals = Animal.query.limit(10).all()

    return True

@app.route('/animals/<animal_id>')
def location_show(location_id):
    """Show a location and its details."""

    location = Location.query.get_or_404(location_id)

    return render_template('location-view.html', location=location)
