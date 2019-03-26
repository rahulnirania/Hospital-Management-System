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