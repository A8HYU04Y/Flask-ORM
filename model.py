from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()
##app = Flask(__name__)

class Flight(db.Model): ## Flight Table
	__tablename__="flights"
	id=db.Column(db.Integer,primary_key=True)
	origin=db.Column(db.String,nullable=False)
	destination=db.Column(db.String,nullable=False)
	duration=db.Column(db.Integer,nullable=False)

class Passenger(db.Model):## Passenger Table
    __tablename__="passengers"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    flight_id=db.Column(db.Integer,db.ForeignKey("flights.id"),nullable=False)





