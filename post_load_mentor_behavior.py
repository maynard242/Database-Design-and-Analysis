#/usr/bin/env python3

# Program to create table mentor_behavior and load from csv 

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS mentor_behavior
	(mentor_persona_id INT,
	pair_id INT,
	mentor_user_id INT,
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
	
sqlstr = "COPY mentor_behavior FROM STDIN DELIMITER ',' CSV"
with open('/home/levi/MIDS/Project/Table_3_mentor_behavior.csv') as f:
    cur.copy_expert(sqlstr, f)
conn.commit()
