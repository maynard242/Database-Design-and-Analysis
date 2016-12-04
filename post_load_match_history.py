#/usr/bin/env python3

# Program to create table match_history and load from csv 

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS match_history
	(pair_id INT,
	mentee_persona_id INT,
	mentee_user_id INT,
	mentor_persona_id INT,
	mentor_user_id	INT,
	member TEXT,
	school TEXT,
	grad_yr	INT,
	Class TEXT,
	prog_type TEXT,
	match_start_date DATE,
	match_end_date	DATE,
	length_of_match_in_days	INT,
	match_closure_reason_control TEXT,
	match_closure_reason_super TEXT,
	match_closure_reason_sub TEXT);''')
conn.commit()
	
sqlstr = "COPY match_history FROM STDIN DELIMITER ',' CSV"
with open('/home/levi/MIDS/Project/Table_1_match_history.csv') as f:
    cur.copy_expert(sqlstr, f)
conn.commit()


