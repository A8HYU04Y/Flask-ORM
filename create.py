from flask import Flask,render_template,request
from model import *
from flask_sqlalchemy import SQLAlchemy
import csv
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "" ## Database URI

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
	db.create_all() ## creating tables
def insert(): ## INSERT INTO
	with open("flights.csv") as f:
		reader=csv.reader(f)
		for origin,destination,duration in reader:
			flight=Flight(origin=origin,destination=destination,duration=duration)
			db.session.add(flight)
			print(f"Added Flight from {origin} to {destination} lasting {duration} ")
		db.session.commit()
def select(): ##SELECT * QUERY
	passengers=Passenger.query.all() ## in case of WHERE clause Flight.query.filter_by(filter).all() ...for filter other than PKey and !=
	for passenger in passengers:## Note : In case of SELCT COUNT(*)  >>>> Flight.query.filter_by(filter).count()
		print(f"{passenger.name} on flight {passenger.flight_id}")
	db.session.commit()
def Like():
    flights=Flight.query.filter(Flight.origin.like("%A%")).all()
    for flight in flights:
    	print(f"{flight.origin}")
    db.session.commit()
## "%a%" string sequence to be checked    
## In case of PKey and WHERE clause Flight.query.get(PKey)
## In case of inequality in WHERE clause only filter() is used instead of filter_by()
##eg: flights=Flight.query.filter(origin != "Paris").all()
## To DELETE flight=Flight.query.get(id) -->> db.session.delete(flight)
## For SELECT * FROM Flight WHERE origin IN ('TOKYO','PARIS')
## >>>> Flight.query.filter(Flight.origin.in_(["TOKYO","PARIS"])).all() NOTE: in_ is used as "in" is already a keyword in python
## >>>> to join db.session.query(Flight,Passenger).filter(Flight.id==Passenger.flight_id).all()
if __name__=="__main__":
	with app.app_context():
	##  select() 
		
	##	Like()
	##	main()
	##	insert()

		
