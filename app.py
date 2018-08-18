from flask import Flask,render_template,request
from model import *
from flask_sqlalchemy import SQLAlchemy
import csv
app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:abhyuday@localhost/lec4"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
@app.route('/')
def index():
	flights=Flight.query.all()
	return render_template('index.html',flights=flights)
@app.route('/book',methods=['POST'])
def book():
	name=request.form.get('name')
	try:
		flight_id=int(request.form.get('flight_id'))
	except ValueError:
		return render_template("Error.html")
	flight=Flight.query.get(flight_id)
	if flight is None:
	    return render_template('Error.html')
	passenger=Passenger(name=name,flight_id=flight_id)
	db.session.add(passenger)
	db.session.commit()
	return render_template('Success.html')    	
@app.route('/flights')
def flights():
	flights=Flight.query.all()
	return render_template("Flights.html",flights=flights)
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
	flight=Flight.query.get(flight_id)
	if flight is None:
		return render_template("Error.html",message="No such flights with ID "+str(flight_id))
	passengers=Passenger.query.filter_by(flight_id=flight_id).all()
	return render_template("Flight.html",flights=flight,passengers=passengers)	
if __name__=="__main__":
	app.run(debug=True)
	##  with app.app_context():
	##	select()
	##	Like()
	##	main()
	##	insert()

		
