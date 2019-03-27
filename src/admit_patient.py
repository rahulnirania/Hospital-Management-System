import pymysql
db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

from add_util import add_into_table
from modify_util import modify_table_row

def admit(ward_no, bed_no, patient_id, date_of_admission, name, doctor_name):
	sql_query = "select patient_id from Bed where ward_id = " + ward_no + " and bed_id = " + bed_no + ";"
	try:
		cursor.execute(sql_query)
		result = cursor.fetchone()
		print(result)
		if (result[0] == None):
			# admit the patient
			add_into_table("Inpatient", {
				'patient_id': patient_id,
				'bed_id': bed_no,
				'date_of_admission': date_of_admission
			})
			# update bed status
			modify_table_row("Bed", {"ward_id": ward_no, "bed_id": bed_no}, {"patient_id": patient_id})
			return 1
		else:
			return 2	
	except:
		print("ERROR: \n" + sql_query)
		return -1