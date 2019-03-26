-- create user 'admin'@'localhost' identified by 'admin';
create database assignment_2;

use assignment_2;

grant all privileges on assignment_2.* to 'admin'@'localhost';

CREATE TABLE Injury_Record (
	ID INT NOT NULL,
	Date datetime,
	Description varchar(200),
	PRIMARY KEY (ID)
);

CREATE TABLE Team (
	Coach varchar(100),
	Name varchar(100),
	Team_ID INT NOT NULL,
	Player_ID INT,
	PRIMARY KEY (Team_ID)
	-- FOREIGN KEY (Player_ID) REFERENCES Player(Player_ID)
);

CREATE TABLE Player (
	Name varchar(100) NOT NULL,
	Position varchar(100),
	Skill_Level varchar(100),
	Player_ID INT NOT NULL,
	Team_ID INT,
	PRIMARY KEY (Player_ID),
	FOREIGN KEY (Team_ID) REFERENCES Team(Team_ID)
);

CREATE TABLE has_injury (
	Player_ID INT NOT NULL,
	Injury_ID INT NOT NULL,
	PRIMARY KEY (Player_ID, Injury_ID),
	FOREIGN KEY (Player_ID) REFERENCES Player (Player_ID),
	FOREIGN KEY (Injury_ID) REFERENCES Injury_Record (ID)
);

ALTER TABLE Team ADD CONSTRAINT FOREIGN KEY (Player_ID) REFERENCES Player (Player_ID);

CREATE TABLE Game (
	Host_ID INT NOT NULL,
	Guest_ID INT NOT NULL,
	Date datetime NOT NULL,
	Score varchar(50) NOT NULL,
	PRIMARY KEY (Host_ID, Guest_ID, Date)
);