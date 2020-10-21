from forms import *
from flask_wtf import Form
from logging import Formatter, FileHandler
import logging
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask import Flask, render_template, request, Response, flash, redirect, url_for
import babel
import dateutil.parser
import json
from flask_migrate import Migrate
import datetime
#from posix import abort
from enum import Enum
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import case


db = SQLAlchemy()


class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(
        db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))


class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #area = db.Column(db.Integer, db.ForeignKey('Area.id'), nullable=True)
    city = db.Column(db.String, nullable=True)
    state = db.Column(db.String, nullable=True)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(120)), nullable=True)
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    #shows = db.relationship('Show', backref='venue', lazy=True)
    upcoming_shows = db.relationship("Show",
                                     primaryjoin="and_(Venue.id==Show.venue_id, "
                                     "Show.start_time >= func.current_date())")
    past_shows = db.relationship("Show",
                                 primaryjoin="and_(Venue.id==Show.venue_id, "
                                 "Show.start_time < func.current_date())")


# https://stackoverflow.com/questions/64403117/how-to-call-an-attribute-inside-the-model-in-flask-sqlalchemy
    # @hybrid_property
    # def upcoming_shows(self):
    #     upcoming_shows = Show.query.filter(Show.venue_id == self.id).filter(
    #         Show.start_time >= db.func.current_date()).all()
    #     return upcoming_shows

    # @hybrid_property
    # def past_shows(self):
    #     past_shows = Show.query.filter(Show.venue_id == self.id).filter(
    #         Show.start_time < db.func.current_date()).all()
    #     return past_shows


    @hybrid_property
    def upcoming_shows_count(self):
        upcoming_shows_count = Show.query.filter(Show.venue_id == self.id).filter(
            Show.start_time >= db.func.current_date()).count()
        return upcoming_shows_count

    @hybrid_property
    def past_shows_count(self):
        past_shows_count = Show.query.filter(Show.venue_id == self.id).filter(
            Show.start_time < db.func.current_date()).count()
        return past_shows_count


class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    #area = db.Column(db.Integer, db.ForeignKey('Area.id'), nullable=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    phone = db.Column(db.String(120))
    db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500))
    genres = db.Column(db.ARRAY(db.String(120)))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artist', lazy=True)

    @hybrid_property
    def upcoming_shows(self):
        upcoming_shows = Show.query.filter(Show.artist_id == self.id).filter(
            Show.start_time >= db.func.current_date()).all()
        return upcoming_shows

    @hybrid_property
    def past_shows(self):
        past_shows = Show.query.filter(Show.artist_id == self.id).filter(
            Show.start_time < db.func.current_date()).all()
        return past_shows

    @hybrid_property
    def upcoming_shows_count(self):
        upcoming_shows_count = Show.query.filter(Show.artist_id == self.id).filter(
            Show.start_time >= db.func.current_date()).count()
        return upcoming_shows_count
# https://stackoverflow.com/questions/8895208/sqlalchemy-how-to-filter-date-field

    @hybrid_property
    def past_shows_count(self):
        past_shows_count = Show.query.filter(Show.artist_id == self.id).filter(
            Show.start_time < db.func.current_date()).count()
        return past_shows_count


# class Area(db.Model):
#     __tablename__ = 'Area'
#     id = db.Column(db.Integer, primary_key=True)
#     # name = db.Column(db.String)
#     city = db.Column(db.String(120))
#     state = db.Column(db.String(120))
#     venues = db.relationship('Venue', backref='Area')
#     artists = db.relationship('Artist', backref='Area')
