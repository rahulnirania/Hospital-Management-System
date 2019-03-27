import pymysql
db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

# function to prettify the output obtained by using cursor.fetchall()
def pretty_print(cursor, data=None, rowlens=0):
    d = cursor.description
    if not d:
        print("#### NO RESULTS ###")
    names = []
    lengths = []
    rules = []
    if not data:
        data = cursor.fetchall(  )
    for dd in d:    # iterate over description
        l = dd[1]
        if not l:
            l = 12            # or default arg ...
        l = max(l, len(dd[0])) # Handle long names
        names.append(dd[0])
        lengths.append(l)
    for col in range(len(lengths)):
        if rowlens:
            rls = [len(row[col]) for row in data if row[col]]
            lengths[col] = max([lengths[col]]+rls)
        rules.append("-"*lengths[col])
    format = " ".join(["%%-%ss" % l for l in lengths])
    result = [format % tuple(names)]
    result.append(format % tuple(rules))
    for row in data:
        result.append(format % row)
    print("\n".join(result))
    
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
