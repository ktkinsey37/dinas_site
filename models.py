"""SQLAlchemy models for Dina's Site."""

from datetime import date

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """A user for the site."""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
                db.Text,
                nullable=False,
                unique=True
    )

    password = db.Column(
            db.Text,
            nullable=False,
    )

    authority = db.Column(
                db.Text,
                nullable=False,
                default="user"
    )

    def __repr__(self):
        return f"<User #{self.id}: {self.username}>"

    @classmethod
    def signup(cls, username, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(
            username=username,
            password=hashed_pwd
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

class Item(db.Model):
    """An item for the store."""

    __tablename__ = 'items'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )

    name = db.Column(
            db.Text,
            nullable=False,
            unique=True
    )

    description = db.Column(
                db.Text,
                default=""
    )

    color = db.Column(
                db.Text,
                nullable=False,
    )

    weight = db.Column(
                db.Float,
                nullable=False
    )
    
    length = db.Column(
                    db.Float,
                    nullable=False
    )

    image_url = db.Column(
                db.Text,
                default=""
                # NEED A DEFAULT IMAGE
    )

    price = db.Column(
                    db.Float,
                    nullable=False
    )

    for_sale = db.Column(
                db.Boolean,
                nullable=False,
                default=True
    )

    held = db.Column(
                db.Boolean,
                nullable=False,
                default=False
    )

    out_of_stock = db.Column(
                db.Boolean,
                nullable=False,
                default=False
    )

    def __repr__(self):
        return f"<Item #{self.id}: {self.name}, ${self.price}>"

class Animal(db.Model):
    """An animal for the store."""

    __tablename__ = 'animals'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )

    name = db.Column(
            db.Text,
            nullable=False,
            unique=True
    )

    description = db.Column(
                db.Text,
                default=""
    )

    species = db.Column(
                db.Text,
                nullable=False,
    )

    morph = db.Column(
                db.Text,
                nullable=False,
    )

    coloration_pattern = db.Column(
                db.Text,
                nullable=False,
    )

    # Store as alphabetized list of strings stringified together, then regex'd back out on /nbsp or w/e

    colors = db.Column(
                db.Text,
                nullable=False,
    )

    birthdate = db.Column(
                db.Date,
                nullable=False,
                default=date.today()
    )

    parent_one = db.Column(
                db.Integer,
                db.ForeignKey('animals.id')
    )

    parent_two = db.Column(
                    db.Integer,
                    db.ForeignKey('animals.id'),
    )
    
    weight = db.Column(
                    db.Float,
                    nullable=False
    )
    
    length = db.Column(
                    db.Float,
                    nullable=False
    )

    image_url = db.Column(
                db.Text,
                default=""
    )

    price = db.Column(
                    db.Float,
                    nullable=False
    )

    for_sale = db.Column(
                db.Boolean,
                nullable=False,
                default=True
    )

    held = db.Column(
                db.Boolean,
                nullable=False,
                default=False
    )

    out_of_stock = db.Column(
                db.Boolean,
                nullable=False,
                default=False
    )

    def __repr__(self):
        return f"<Animal #{self.id}: {self.name}, {self.morph}. Parents: {self.parent_one}, {self.parent_two}>"

class Event(db.Model):
    """An event for the website."""

    __tablename__ = 'events'

    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False
    )

    title = db.Column(
            db.Text,
            nullable=False,
            unique=True
    )

    description = db.Column(
                db.Text,
                default=""
    )

    starttime = db.Column(
                db.Text,
                nullable=False,
    )

    endtime = db.Column(
                db.Text,
                nullable=False,
    )

    image_url = db.Column(
                db.Text,
                default=""
    )

    def __repr__(self):
        return f"<Animal #{self.id}: {self.name}, {self.morph}. Parents: {self.parent_one}, {self.parent_two}>"


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
