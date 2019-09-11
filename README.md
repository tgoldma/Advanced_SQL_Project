# Climate Analysis and Exploration

In this project I used Python and SQLAlchemy to do basic climate analysis and data exploration on a climate database. All of the analysis I complted was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


I used a starter notebook and hawaii.sqlite files to complete my climate analysis and data exploration.
I choose a start date and end date for my trip.
Used SQLAlchemy create_engine to connect to my sqlite database.
Used SQLAlchemy automap_base() to reflect the tables into classes and saved a reference to those classes called Station and Measurement.

Precipitation Analysis

I designed a query to retrieve the last 12 months of precipitation data.
Only the date and prcp values were selected.
Loaded the query results into a Pandas DataFrame and set the index to the date column.
Sorted the DataFrame values by date.
Plotted the results using the DataFrame plot method.
Used Pandas to print the summary statistics for the precipitation data.


Station Analysis

Designed a query to calculate the total number of stations.
Designed a query to find the most active stations.

Listed the stations and observation counts in descending order.

Designed a query to retrieve the last 12 months of temperature observation data (tobs).


Filtered by the station with the highest number of observations.
Ploted the results as a histogram with bins=12.



Climate App

I designed a Flask API based on the queries that you have just developed.

I converted the query results to a Dictionary using date as the key and prcp as the value.
Return the JSON representation of your dictionary, and returned a JSON list of stations from the dataset.

Queried for the dates and temperature observations from a year from the last data point.
Returned a JSON list of Temperature Observations (tobs) for the previous year.

Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, I calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
