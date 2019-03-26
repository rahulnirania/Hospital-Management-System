-- create user 'admin'@'localhost' identified by 'admin';
create database flights;
use flights;
grant all privileges on flights.* to 'admin'@'localhost';

CREATE TABLE Airport (
	Code VARCHAR(30) NOT NULL,
	Name VARCHAR(100),
	City VARCHAR(100),
	Country VARCHAR(100),
	PRIMARY KEY (Code)
);

CREATE TABLE Flight (
	Number VARCHAR(30) NOT NULL,
	Airline VARCHAR(100),
	From_Airport_Code VARCHAR(30) NOT NULL,
	To_Airport_Code VARCHAR(30) NOT NULL,
	PRIMARY KEY (Number),
	FOREIGN KEY (From_Airport_Code) REFERENCES Airport (Code),
	FOREIGN KEY (To_Airport_Code) REFERENCES Airport (Code)
);

CREATE TABLE Reservation (
	Flight_Number VARCHAR(30) NOT NULL,
	Seat_Number VARCHAR(10) NOT NULL,
	Date DATE NOT NULL,
	Passenger_Name VARCHAR(100) NOT NULL,
	PRIMARY KEY (Flight_Number, Seat_Number, Date),
	FOREIGN KEY (Flight_Number) REFERENCES Flight (Number)
);