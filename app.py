import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
#database
engine = create_engine("sqlite:///Resources/hawaii.sqlite",connect_args={'check_same_thread':False})


Base = automap_base()

Base.prepare(engine, reflect=True)

# Save to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


session = Session(engine)

# Setup Flask

app = Flask(__name__)
#routes

@app.route("/")
def welcome():
    #all api routes#
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Query date and prcp
    results = session.query(Measurement).all()

    # Create dictionary 
    all_precipitation = []
    for day in results:
        precipitation_dict = {}
        precipitation_dict["date"] = Measurement.date
        precipitation_dict["prcp"] = Measurement.prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)


@app.route("/api/v1.0/stations")
def stations():

    # Query all stations
    results = session.query(Station.station).all()

    # Make list of tuples into a regular list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():

    #Do a query for all the stations 
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date > '2016-08-31').all()

    all_stations = list(np.ravel(results))

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>" and "/api/v1.0/<start>/<end>")
def calc_temps(start_date, end_date):
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

print(calc_temps('2012-01-27', '2012-02-05'))

#return jsonify(calc_temps)

if __name__ == '__main__':
    app.run(debug=True)