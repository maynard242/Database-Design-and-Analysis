#/usr/bin/env python3

# Program to create table mentor_demo and load from csv 

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS mentor_demo
	(mentor_persona_id INT,
	mentor_user_id INT,
	Racial_Group TEXT,
	Gender TEXT,
	Application_Source TEXT,
	Birthdate DATE,
	Lives_in_Borough TEXT,
	Current_Career TEXT,
	Date_Matched DATE,
	Date_Match_End DATE,
	Have_Children INT, 
	Current_Occcupation TEXT,
	Marital_Status TEXT,
	Level_of_Education TEXT,
	Partner_Site TEXT,
	School_cohort_id INT,
	program_type TEXT,
	Mailing_Zip_PostalCode INT,
	Language_other_than_English TEXT,
	Parent_Guardian_College_Degree TEXT,
	College_Majors TEXT,
	How_did_you_hear_about_iMentor TEXT,
 	Employer TEXT,
	Colleges_Attended TEXT);''')
conn.commit()
	
sqlstr = "COPY mentor_demo FROM STDIN DELIMITER ',' CSV"
with open('/home/levi/MIDS/Project/Table_2_mentor_demo.csv') as f:
    cur.copy_expert(sqlstr, f)
conn.commit()
