-- create user 'admin'@'localhost' identified by 'admin';
create database hms;
use hms;
grant all privileges on hms.* to 'admin'@'localhost';

CREATE TABLE Patient (
	patient_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	gender ENUM ('M', 'F') NOT NULL,
	dob DATE NOT NULL,
	weight FLOAT NOT NULL,
	admitted ENUM ('yes', 'no'),
	mother_name VARCHAR(50) NOT NULL,
	contact_no VARCHAR(15) NOT NULL,
	address VARCHAR(100) NOT NULL,
	PRIMARY KEY (patient_id)
);

CREATE TABLE Doctor (
	doctor_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	dob DATE NOT NULL,
	gender ENUM ('M', 'F') NOT NULL,
	department VARCHAR(50) NOT NULL,
	qualification VARCHAR(50) NOT NULL,
	contact_no VARCHAR(15) NOT NULL,
	address VARCHAR(100) NOT NULL,
	email VARCHAR(20) NOT NULL,
	salary INT NOT NULL,
	PRIMARY KEY (doctor_id)
);

CREATE TABLE Staff (
	staff_id INT NOT NULL AUTO_INCREMENT,
	type ENUM ('Consultant', 'Intern', 'Nurse'),
	name VARCHAR(50) NOT NULL,
	dob DATE NOT NULL,
	gender ENUM ('M', 'F') NOT NULL,
	address VARCHAR(100) NOT NULL,
	contact_no VARCHAR(15) NOT NULL,
	salary INT NOT NULL,
	qualification VARCHAR(50) NOT NULL,
	PRIMARY KEY (staff_id)
);

CREATE TABLE Ward (
	ward_id INT NOT NULL AUTO_INCREMENT,
	no_of_beds INT NOT NULL,
	class VARCHAR(10) NOT NULL,
	current_status INT NOT NULL,
	PRIMARY KEY (ward_id)
);

CREATE TABLE Bed (
	bed_id INT NOT NULL AUTO_INCREMENT,
	ward_id INT NOT NULL,
	patient_id INT NOT NULL,
	PRIMARY KEY (bed_id),
	FOREIGN KEY (ward_id) REFERENCES Ward (ward_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id)
);	

CREATE TABLE Inpatient (
	patient_id INT NOT NULL,
	bed_id INT NOT NULL,
	date_of_admission DATE NOT NULL,
	date_of_discharge DATE NOT NULL,
	PRIMARY KEY (patient_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
	FOREIGN KEY (bed_id) REFERENCES Bed (bed_id)
);

CREATE TABLE Lab_Report (
	lab_id INT NOT NULL,
	report_id INT NOT NULL AUTO_INCREMENT,
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	date DATE NOT NULL,
	test_type VARCHAR(100) NOT NULL,
	result ENUM ('positive', 'negative'),
	amount INT NOT NULL,
	PRIMARY KEY (report_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
	FOREIGN KEY (doctor_id) REFERENCES Doctor (doctor_id)
);

CREATE TABLE Stock (
	stock_id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(100) NOT NULL,
	price INT NOT NULL,
	description VARCHAR(100) NOT NULL,
	quantity_available INT NOT NULL,
	type ENUM('Medicine', 'Equipment'),
	PRIMARY KEY (stock_id)
);

CREATE TABLE Patient_Equipment (
	patient_id INT NOT NULL,
	equipment_id INT NOT NULL,
	PRIMARY KEY (patient_id, equipment_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
	FOREIGN KEY (equipment_id) REFERENCES Stock (stock_id)
);

CREATE TABLE Patient_Bill (
	patient_id INT NOT NULL,
	eq_bill_amount INT NOT NULL,
	tr_bill_amount INT NOT NULL,
	to_bill_amount INT NOT NULL,
	PRIMARY KEY (patient_id)
);

CREATE TABLE Patient_Doctor (
	patient_id INT NOT NULL,
	doctor_id INT NOT NULL,
	PRIMARY KEY (patient_id, doctor_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
	FOREIGN KEY (doctor_id) REFERENCES Doctor (doctor_id)
);

CREATE TABLE Patient_Staff (
	patient_id INT NOT NULL,
	staff_id INT NOT NULL,
	PRIMARY KEY (patient_id, staff_id),
	FOREIGN KEY (patient_id) REFERENCES Patient (patient_id),
	FOREIGN KEY (staff_id) REFERENCES Staff (staff_id)
);