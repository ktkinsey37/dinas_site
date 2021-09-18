from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField
from wtforms.fields.core import BooleanField, FloatField
from wtforms.validators import DataRequired, Email, Length, email_validator

class AddAdmin(FlaskForm):
    """Form for one admin user to add another"""

    name = StringField('User name of prospective admin', validators=[DataRequired()])

class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    # email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class ItemForm(FlaskForm):
    """Form for adding locations."""

    name = StringField('Name of item', validators=[DataRequired()],  render_kw={"placeholder": "Eg: Widget"})
    description = TextAreaField('Brief description of the item', render_kw={"placeholder": "Eg: A tool used for a wide variety of reptile-related applications."})
    color = StringField('Latitude', validators=[DataRequired()], render_kw={"placeholder": "(can list multiple colors) Eg: Teal, Black, Red, Yellow"})
    weight = FloatField('Longitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: 3 oz"})
    length = FloatField('Item Length', validators=[DataRequired()], render_kw={"placeholder": "Eg 2.4 in"}) # Do you have a preference for metric or std?
    image_url = StringField('URL of the image') # Would you prefer onsite hosting or linking to a separate site ie Instagram
    price = FloatField('Price of the item')
    availability = RadioField('Item Availability', choices=[('sale','For Sale'), ('held','Held'), ('out', 'Out of Stock')], validators=[DataRequired()])

class ItemEditForm(FlaskForm):
    """Form for adding locations."""

    name = StringField('Name of Location', validators=[DataRequired()],  render_kw={"placeholder": "Eg: Indian Creek"})
    location = StringField('Brief description of how to get to location', render_kw={"placeholder": "Eg: An hour south of Moab, UT"})
    latitude = FloatField('Latitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: 38.03535"})
    longitude = FloatField('Longitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: -109.56968"})
    image_url = StringField('(Optional) Image URL', render_kw={"placeholder": "Eg: Indian Creek"})
    description = TextAreaField('Brief description of the area')
    env = RadioField('Climbing Environment', choices=[('sand','Sandstone'), ('alp','Alpine'), ('none', 'Neither')], validators=[DataRequired()])

class AnimalForm(FlaskForm):
    """Form for editing locations."""

    name = StringField('Name of Location', validators=[DataRequired()],  render_kw={"placeholder": "Eg: Indian Creek"})
    location = StringField('Brief description of how to get to location', render_kw={"placeholder": "Eg: An hour south of Moab, UT"})
    latitude = FloatField('Latitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: 38.03535"})
    longitude = FloatField('Longitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: -109.56968"})
    image_url = StringField('(Optional) Image URL', render_kw={"placeholder": "Eg: Indian Creek"})
    description = TextAreaField('Brief description of the area')
    env = RadioField('Climbing Environment', choices=[('sand','Sandstone'), ('alp','Alpine'), ('none', 'Neither')], validators=[DataRequired()])

class AnimalEditForm(FlaskForm):
    """Form for editing locations."""

    name = StringField('Name of Location', validators=[DataRequired()],  render_kw={"placeholder": "Eg: Indian Creek"})
    location = StringField('Brief description of how to get to location', render_kw={"placeholder": "Eg: An hour south of Moab, UT"})
    latitude = FloatField('Latitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: 38.03535"})
    longitude = FloatField('Longitude', validators=[DataRequired()], render_kw={"placeholder": "Eg: -109.56968"})
    image_url = StringField('(Optional) Image URL', render_kw={"placeholder": "Eg: Indian Creek"})
    description = TextAreaField('Brief description of the area')
    env = RadioField('Climbing Environment', choices=[('sand','Sandstone'), ('alp','Alpine'), ('none', 'Neither')], validators=[DataRequired()])