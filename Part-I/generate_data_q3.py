import pymysql
from faker import Faker
import factory
import random

db = pymysql.connect("localhost", "admin", "admin", "flights")
cursor = db.cursor()

fake = Faker()

# general function to add a row into a table
def add_into_table(table_name, row):
	# table_name is the table name, row is the dictionary containing key and value mappings
	sql_query = "INSERT INTO " + table_name + " Values("
	for key in row.keys():
		if (row[key] == 'NULL'):
			sql_query += row[key]
		elif (type(row[key]) == str):
			sql_query += '\''
			sql_query += row[key]
			sql_query += '\''
		else:	
			sql_query += str(row[key])
		sql_query += ','
	sql_query = sql_query[:-1]
	sql_query += ');'
	# print(sql_query);
	try:
   		# Execute the SQL command
	   	cursor.execute(sql_query)
	   	# Commit your changes in the database
	   	db.commit()
	except:
   		# Rollback in case there is any error
   		db.rollback()

airports = []
num_airports = 10
for i in range(num_airports):
	code = fake.country_code()
	name = fake.street_name()
	city = fake.city()
	country = fake.country()
	airports.append({
		'Code': code, 
		'Name': name, 
		'City': city,
		'Country': country, 
	})
	add_into_table('Airport', airports[i])

flights = []
num_flights = 20
airlines = ["Indigo", "Jet Airways", "Air India", "Spice Jet"]
for i in range(num_flights):
	Number = fake.random_letter() + fake.random_letter() + str(fake.random_digit()) + str(fake.random_digit())
	Airline = airlines[random.randint(0, 3)]
	airport_from = random.randint(0, num_airports - 1)
	From_Airport_Code = airports[airport_from]['Code']
	To_Airport_Code = airports[(airport_from + 1)%num_airports]['Code']
	
	flights.append({
		'Number': Number,
		'Airline': Airline,
		'From_Airport_Code': From_Airport_Code,
		'To_Airport_Code': To_Airport_Code
	})
	add_into_table('Flight', flights[i])

reservations = []
num_reservations = 30
for i in range(num_reservations):
	flight_index = random.randint(0, num_flights - 1)
	Flight_Number = flights[flight_index]['Number']
	Seat_Number = fake.random_element(elements=('A', 'B', 'C')) + str(random.randint(1, 30))
	Date = fake.date()
	Passenger_Name = fake.name()
	reservations.append({
		'Flight_Number': Flight_Number,
		'Seat_Number': Seat_Number,
		'Date': Date,
		'Passenger_Name': Passenger_Name
	})
	add_into_table('Reservation', reservations[i])