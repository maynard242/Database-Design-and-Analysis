#/usr/bin/env python3

# Program to create table mentee_behavior and load from csv 

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS mentee_behavior_2
	(mentee_persona_id INT,
	pair_id INT,
	mentee_user_id INT,
	lesson_id INT,
	curriculum_sequence TEXT,
	lesson_launch TIMESTAMP,
	lesson_close TIMESTAMP,
	user_begin TIMESTAMP,
	user_first_sub TIMESTAMP,
	time_on_canvas_sub_1 INTERVAL,
	user_most_recent_sub TIMESTAMP,
	canvas_word_cnt INT,
	convo_count INT,
	convo_word_cnt INT);''')
conn.commit()
	
sqlstr = "COPY mentee_behavior_2 FROM STDIN DELIMITER ',' CSV"
with open('/Users/nwchen24/Desktop/UC_Berkeley/Storing_and_Retrieving_Data/Final Project/Data from iMentor/2016-11-01 Message Traffic/mentee_platform_behavior11216_forload.csv') as f:
    cur.copy_expert(sqlstr, f)
conn.commit()
