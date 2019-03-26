import pymysql

# connect with the database
db = pymysql.connect("localhost", "admin", "admin", "flights")
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

def flight_numbers():
    select = "select Number from Flight, Airport "
    condition = """where Airport.Country = \"India\" and
                    Flight.From_Airport_Code = Airport.Code;
                """
    sql_query = select + condition  
    cursor.execute(sql_query)
    data = cursor.fetchall()
    pretty_print(cursor, data)


def passengers():
    select = "select Passenger_Name from Reservation "
    condition = """where Date = \"2019-02-11\"
                    and Flight_Number = \"AI 747\";
                """ 
    sql_query = select + condition
    cursor.execute(sql_query)
    data = cursor.fetchall()
    pretty_print(cursor, data)

def flights():
    select = "select * from Flight "
    condition = """where Airline = \"Air India\"
                    or Airline = \"Indigo\";
                """
    sql_query = select + condition
    cursor.execute(sql_query)
    data = cursor.fetchall()
    pretty_print(cursor, data)

print("============================================================================================")
print("Query 1: List the flight numbers of flights that take off from India")
flight_numbers()
print("============================================================================================")

print("Query 2: List the passengers who are travelling on Feb 11, 2019 by flight number AI 747")
passengers()
print("============================================================================================")

print("Query 3: List all the flight information for Air India and Indigo")
flights()
print("============================================================================================")
