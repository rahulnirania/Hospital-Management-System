from add_util import add_into_table

def add_patient(Name, Gender, DOB, Mother_name, Contact, Address, Weight, Admitted):
	patient = {
		'name': Name,
		'gender': Gender,
		'dob': DOB,
		'weight': Weight,
		'admitted': Admitted,
		'mother_name': Mother_name,
		'contact_no': Contact,
		'address': Address
	}
	add_into_table("Patient", patient)