import pymysql
from faker import Faker
import factory
import random

db = pymysql.connect("localhost", "admin", "admin", "hms")
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