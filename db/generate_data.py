import pymysql
from faker import Faker
import factory
import random
from add_util import add_into_table

db = pymysql.connect("localhost", "admin", "admin", "hms")
cursor = db.cursor()

fake = Faker()

medicines = []
num_medicines = 10
names = ["synthroid", "crestor", "ventolin HFA", "nexium", "advair diskus", "lantus solostar", "vyvnase", "lyrica", "spiriva handihaler", "januvia"]
for i in range(num_medicines):
	name = names[i]
	price = random.randint(100, 500)
	description = fake.text(max_nb_chars=50, ext_word_list=None)
	quantity_available = random.randint(1, 10)
	type = "Medicine"
	medicines.append({
		'name': name,
		'price': price,
		'description': description,
		'quantity_available': quantity_available,
		'type': type
	})
	add_into_table("Stock", medicines[i])

doctors = []
num_doctors = 100
departments = ["accident and emergency", "anaesthetics", "breast screening", "cardiology", "chaplaincy", "critical care", "diagnostic imaging", "discharge lounge", "ear nose and throat", "elderly services", "gastroenterology", "surgery", "gynaecology", "haeamatology", "maternity", "microbiology", "nepgrology", "neurology", "nutrition and dietics", "obstetrics", "oncology", "ophthalmology", "orthopaedics"]
quals = ["MBBS", "MD", "MCM", "MPhil", "MM", "MSurg", "MSc"]
for i in range(num_doctors):
	dob = fake.date()
	gender = fake.random_element(elements=('M', 'F'))
	if (gender == 'M'):
		name = fake.name_male()
	else:
		name = fake.name_female()
	department = departments[random.randint(0, len(departments) - 1)]
	qualification = quals[random.randint(0, len(quals) - 1)]
	contact_no = fake.phone_number()
	address = fake.address()
	email = fake.email()
	salary = random.randint(100000, 1000000)
	doctors.append({
		'name': name,
		'dob': dob,
		'gender': gender,
		'department': department,
		'qualification': qualification,
		'contact_no': contact_no,
		'address': address,
		'email': email,
		'salary': salary
	})
	add_into_table("Doctor", doctors[i])

staffs = []
num_staff = 100
quals = ["MBBS", "MD", "MCM", "MPhil", "MM", "MSurg", "MSc"]
for i in range(num_doctors):
	dob = fake.date()
	gender = fake.random_element(elements=('M', 'F'))
	if (gender == 'M'):
		name = fake.name_male()
	else:
		name = fake.name_female()
	qualification = quals[random.randint(0, len(quals) - 1)]
	contact_no = fake.phone_number()
	address = fake.address()
	salary = random.randint(10000, 100000)
	type = fake.random_element(elements = ('Consultant', 'Intern', 'Nurse'))
	staffs.append({
		'name': name,
		'dob': dob,
		'gender': gender,
		'type': type,
		'qualification': qualification,
		'contact_no': contact_no,
		'address': address,
		'salary': salary
	})
	add_into_table("Staff", staffs[i])

patients = []
num_patients = 100
for i in range(num_patients):
	name = fake.name()
	dob = fake.date()
	gender = fake.random_element(elements=('M', 'F'))
	weight = random.randint(40, 100)
	admitted = "no"
	mother_name = fake.name_female()
	contact_no = fake.phone_number()
	address = fake.address()
	patients.append({
		'name': name,
		'dob': dob,
		'gender': gender,
		'contact_no': contact_no,
		'address': address,
		'admitted': admitted,
		'mother_name': mother_name,
		'weight': weight
	})
	add_into_table("Patient", patients[i])

wards = []
num_wards = 20
classes = ['I', 'II' , 'III', 'General']
# I - 1 bed
# II - 2 to 5 bed
# III - 5 to 10 bed
# General - 10 to 25 bed
for i in range(num_wards):
	Class = classes[random.randint(0, len(classes) - 1)]
	if (Class == "I"):
		no_of_beds = 1
	elif (Class == "II"):
		no_of_beds = random.randint(2, 5)
	elif (Class == "III"):
		no_of_beds = random.randint(5, 10)
	else:
		no_of_beds = random.randint(10, 25)
	current_status = 0
	wards.append({
		'no_of_beds': no_of_beds,
		'class': Class,
		'current_status': current_status
	})
	add_into_table("Ward", wards[i])
