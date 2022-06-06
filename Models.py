# import datetime
# # from email.policy import default
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects.postgresql import ARRAY

# db = SQLAlchemy()

# class Venue(db.Model):
#     __tablename__ = 'venue'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     address = db.Column(db.String(120))
#     phone = db.Column(db.String(120))
#     image_link = db.Column(db.String(500))
#     facebook_link = db.Column(db.String(120))
#     seeking_venue = db.Column(db.Boolean, nullable = False, default = False)
#     seeking_description = db.Column(db.String)
#     image_link = db.Column(db.String(500), nullable = False)
#     show = db.relationship('Show', backref='venue', lazy='joined', cascade='all, delete')

#     class Artist(db.Model):
#         __tablename__ = 'artist'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     city = db.Column(db.String(120), nullable=False)
#     state = db.Column(db.String(120), nullable=False)
#     phone = db.Column(db.String(120), nullable=False)
#     genres = db.Column(ARRAY(db.String()), nullable=False,  default=[])
#     website = db.Column(db.String)
#     image_link = db.Column(db.String(500), nullable = False)
#     facebook_link = db.Column(db.String(120))
#     seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
#     seeking_description = db.Column(db.String)
#     show = db.relationship('Show', backref='artist', lazy='joined', cascade='all, delete')

#     class Show(db.Model):
#         __tablename__ = 'show'
#     id = db.Column(db.Integer, primary_key=True)
#     artist_id =db.Column (db.Integer, db.ForeignKey('artist.id'), nullabe=False)
#     venue_id =db.Column (db.Integer, db.ForeignKey('venue.id'), nullabe=False)
#     start_time =db.Column(db.DateTime, default=datetime.datetime.now, nullable=False)