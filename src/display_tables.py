import pymysql
db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

def get_column_from_table(column_name, table_name):
	sql_query = "SELECT "+ column_name + " from " + table_name + ";"
	try:
	   	cursor.execute(sql_query)
	   	result = cursor.fetchall()
	   	return result
	except:
   		print("ERROR: \n" + sql_query)
   		return -1

# print(get_column_from_table("name", "Patient"))

def get_column_from_table_c(column_name, table_name, cond_col, value):
	select = "SELECT "+ column_name + " from " + table_name + " where "
	if (type(value) == str):
		condition = cond_col + " = \"" + value + "\";"
	else:
		condition = cond_col + " = " + value + ";"  
	sql_query = select + condition
	try:
	   	cursor.execute(sql_query)
	   	result = cursor.fetchall()
	   	return result
	except:
   		print("ERROR: \n" + sql_query)
   		return -1

# print(get_column_from_table("name", "Patient"))