from add_util import add_into_table

def add_staff(Name, Gender, DOB, Qual, Contact, Address, email, salary, types):
	staff = {
		'type': types,
		'name': Name,
		'gender': Gender,
		'dob': DOB,
		'contact_no': Contact,
		'address': Address,
		'qualification': Qual,
		'salary': salary
	}
	add_into_table("Staff", staff)