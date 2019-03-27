import pymysql
db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

# general function to add a row into a table
def modify_table_row(table_name, row, new_row):
	# table_name is the table name, row is the dictionary containing key and value mappings
	sql_query = "UPDATE " + table_name + " SET "
	for key in new_row.keys():
		sql_query += key
		sql_query += ' = '
		if (new_row[key] == 'NULL'):
			sql_query += row[key]
		elif (type(new_row[key]) == str):
			sql_query += '\''
			sql_query += row[key]
			sql_query += '\''
		else:	
			sql_query += str(row[key])

	sql_query + " WHERE "
	
	num = len(row.keys())
	ct = 1
	for key in row.keys():
		sql_query += key
		sql_query += ' = '
		if (row[key] == 'NULL'):
			sql_query += row[key]
		elif (type(row[key]) == str):
			sql_query += '\''
			sql_query += row[key]
			sql_query += '\''
		else:	
			sql_query += str(row[key])
		if (ct != num):
			sql_query += " and "
	sql_query += ' ;'
	print(sql_query);
	try:
   		# Execute the SQL command
	   	cursor.execute(sql_query)
	   	# Commit your changes in the database
	   	db.commit()
	except:
   		# Rollback in case there is any error
   		db.rollback()