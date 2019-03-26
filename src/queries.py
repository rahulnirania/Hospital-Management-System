import pymysql
db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

def get_wards_by_class(class_name):
	sql_query = "select ward_id from ward where class = \"" + class_name + "\";"
	try:
	   	cursor.execute(sql_query)
	   	result = cursor.fetchall()
	   	return result
	except:
		print("ERROR: \n" + sql_query)
		return -1

def get_ward_total(ward_id):
	sql_query = "select no_of_beds from ward where ward_id = " + ward_id + ";"
	try:
	   	cursor.execute(sql_query)
	   	result = cursor.fetchall()
	   	return result
	except:
		print("ERROR: \n" + sql_query)
		return -1

def get_ward_avl(ward_id):
	sql_query = "select no_of_beds from ward where ward_id = " + ward_id + ";"
	try:
	   	cursor.execute(sql_query)
	   	result = cursor.fetchall()
	   	return result
	except:
		print("ERROR: \n" + sql_query)
		return -1
