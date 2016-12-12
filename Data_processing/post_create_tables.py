#/usr/bin/env python3

# Program to do create final tables t1_mentor_platform_behavior, t2_mentee_platform_behavor, t3_match_history, t4_demography, 
# t5_imentor_master1516, and t6_zipcodes

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password ="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()


# Table t1_mentor_platform_behavior - draws on mentor_platform; MISSING response time, by_mentor_word_count_zscore, by_mentor_response_time_zscore

cur.execute('''CREATE TABLE IF NOT EXISTS t1_mentor_platform_behavior AS 
SELECT 
	mentor_persona_id, 
	pair_id, 
	lesson_id, 
	canvas_word_cnt, 
	time_on_canvas_sub_1, 
	user_first_sub 
FROM mentor_behavior;''')	
conn.commit()

cur.execute('''ALTER TABLE t1_mentor_platform_behavior ADD response_time INT;''')
conn.commit()

cur.execute('''ALTER TABLE t1_mentor_platform_behavior ADD by_mentor_word_count_zscore FLOAT;''')
conn.commit()

cur.execute('''ALTER TABLE t1_mentor_platform_behavior ADD by_mentor_response_time_zscore FLOAT;''')
conn.commit()

#cur.execute('''ALTER TABLE t1_mentor_platform_behavior ADD PRIMARY KEY(mentor_persona_id);''')
#conn.commit()

# Table t2_mentee_platform_behavior - draws on mentee_platform

cur.execute('''CREATE TABLE IF NOT EXISTS t2_mentee_platform_behavior AS 
SELECT 
	mentee_persona_id, 
	pair_id, 	
	lesson_id, 
	canvas_word_cnt, 
	time_on_canvas_sub_1, 
	user_first_sub 
FROM mentee_behavior;''')	
conn.commit()

#cur.execute('''ALTER TABLE t2_mentee_platform_behavior ADD PRIMARY KEY(mentee_persona_id);''')
#conn.commit()

# Table t3_match_history - draws on match_history_process

cur.execute('''CREATE TABLE IF NOT EXISTS t3_match_history AS 
SELECT * FROM match_history_process;''')
conn.commit()

cur.execute('''ALTER TABLE t3_match_history DROP COLUMN pair_id,
																				 		DROP COLUMN mentee_persona_id,
																				 		DROP COLUMN mentee_user_id,
																				 		DROP COLUMN member,
																				 		DROP COLUMN match_start_date,
																				 		DROP COLUMN match_end_date,
																				 		DROP COLUMN length_of_match_in_days,
																				 		DROP COLUMN match_closure_reason_sub;''')
conn.commit()

#cur.execute('''ALTER TABLE t4_demography ADD PRIMARY KEY(mentor_persona_id);''')
#conn.commit()

# Table t4_demography - draws on mentor_demo_process; Note RENAMED Mailing_Zip to zipcode

cur.execute('''CREATE TABLE IF NOT EXISTS t4_demography AS 
SELECT * FROM mentor_demo_process;''')	
conn.commit()

cur.execute('''ALTER TABLE t4_demography DROP COLUMN Lives_in_Borough,
																				 DROP COLUMN Date_Matched,
																				 DROP COLUMN Date_Match_End,
																				 DROP	COLUMN Partner_Site,
																				 DROP COLUMN School_cohort_id,
																				 DROP COLUMN program_type,
																				 DROP	COLUMN Colleges_Attended;''')
conn.commit()
																				 
cur.execute('''ALTER TABLE t4_demography RENAME Mailing_Zip_PostalCode to zipcode;''')
conn.commit()

#cur.execute('''ALTER TABLE t4_demography ADD PRIMARY KEY(zipcode);''')
#conn.commit()

# Table t5_imentor_master1516 - draws on master_table_process; NOTE mentor_online_freq_1516 undefined

cur.execute('''CREATE TABLE IF NOT EXISTS t5_imentor_master1516 AS 
SELECT 
	most_recent_mentor_persona_id, 
	oop_status, 
	same_eth_mentee, 
	mentor_eth, 
	mentor_fgen, 
	touchpoints, 
	mentor_online_freq, 
	pair_online_freq, 
	pair_meetings, 
	pair_oop_mtgs_1516 
FROM master_table_process;''')	
conn.commit()

cur.execute('''ALTER TABLE t5_imentor_master1516 RENAME most_recent_mentor_persona_id to mentor_persona_id;''')
conn.commit()

#cur.execute('''ALTER TABLE t5_imentor_master1516 ADD PRIMARY KEY(mentor_persona_id);''')
#conn.commit()

# Table t6_zipcodes -  draws on mentor_demo_process; MISSING state

cur.execute('''CREATE TABLE IF NOT EXISTS t6_zipcodes AS 
SELECT 
	Lives_in_Borough, 
	Mailing_Zip_PostalCode 
FROM mentor_demo_process;''')	
conn.commit()

cur.execute('''ALTER TABLE t6_zipcodes RENAME Lives_in_Borough to borough;''')
conn.commit()

cur.execute('''ALTER TABLE t6_zipcodes RENAME Mailing_Zip_PostalCode to zipcode;''')
conn.commit()

cur.execute('''ALTER TABLE t6_zipcodes ADD state TEXT;''')
conn.commit()

#cur.execute('''ALTER TABLE t6_zipcodes ADD PRIMARY KEY(zipcode);''')
#conn.commit()

conn.close()


