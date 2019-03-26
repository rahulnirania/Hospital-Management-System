import pymysql
from faker import Faker
import factory
import random

db = pymysql.connect("localhost", "admin", "admin", "assignment_2")
cursor = db.cursor()

fake = Faker()

# general function to add a row into a table
def add_into_table(table_name, row):
	# table_name is the table name, row is the dictionary containing key and value mappings
	sql_query = "INSERT INTO " + table_name + " Values("
	for key in row.keys():
		if (row[key] == 'NULL'):
			sql_query += row[key]
		elif (type(row[key]) == str):
			sql_query += '\''
			sql_query += row[key]
			sql_query += '\''
		else:	
			sql_query += str(row[key])
		sql_query += ','
	sql_query = sql_query[:-1]
	sql_query += ');'
	# print(sql_query);
	try:
   		# Execute the SQL command
	   	cursor.execute(sql_query)
	   	# Commit your changes in the database
	   	db.commit()
	except:
   		# Rollback in case there is any error
   		db.rollback()

teams = []
num_teams = 10
for i in range(num_teams):
	id = i + 1
	coach = fake.name()
	name = fake.company()
	player_id = 10*i + 1  # captain of team (id = i + 1) is player 10*i + 1
	teams.append({
		'Coach':coach, 
		'Name': name, 
		'Team_ID': id,
		'Player_ID': 'NULL', 
	})
	add_into_table('Team', teams[i])

players = []
num_players = 110 # 11 players in 1 team
positions = ["right wing", "center", "left wing", "defenseman", "defenseman", "goalie"]
levels = ["beginner", "D3", "D2", "D1", "C3", "C2", "C1", "B2", "B1/A", "NHL"]
count = 0
tid = 1
for i in range(num_players):
	Name = fake.name()
	Position = positions[random.randint(0, 5)]
	Skill_Level = levels[random.randint(0, 9)]
	Player_ID = i + 1
	Team_ID = tid
	count += 1
	if (count % 11 == 0):
		tid += 1
	players.append({
		'Name': Name,
		'Position': Position,
		'Skill_Level': Skill_Level,
		'Player_ID': Player_ID,
		'Team_ID': Team_ID
	})
	add_into_table('Player', players[i])

games = []
num_games = 10
for i in range(num_games):
	Host_ID = random.randint(1, num_teams)
	Guest_ID = random.randint(1, num_teams)
	Date = fake.date() + ' ' + fake.time()
	Score = str(random.randint(0, 6)) + '-' + str(random.randint(0, 6))
	games.append({
		'Host_ID': Host_ID,
		'Guest_ID': Guest_ID,
		'Date': Date,
		'Score': Score
	})
	add_into_table('Game', games[i])

injuries = []
num_injuries = 10
common_injuries = ["concussion", "shoulder separation - ac joint injury", "knee ligament injury", "groin strains", "high angle sprain"]
for i in range(num_injuries):
	id = i + 1
	date = fake.date() + ' ' + fake.time()
	description = common_injuries[random.randint(0, 4)]
	injuries.append({
		'ID': id,
		'Date': date,
		'Description': description
	})
	add_into_table('Injury_Record', injuries[i])

num_players_injuries = 10
players_injuries = []
for i in range(num_players_injuries):
	player_id = random.randint(1, num_players)
	injury_id = i + 1
	players_injuries.append({
		'Player_ID': player_id,
		'Injury_ID': injury_id
	})
	add_into_table('has_injury', players_injuries[i])