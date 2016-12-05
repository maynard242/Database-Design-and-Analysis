#/usr/bin/env python3

# Program to do some processing of the match_history table (result = match_history_process

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS match_history_process AS SELECT * FROM match_history;''')	
conn.commit()
	
cur.execute('''DELETE FROM match_history_process WHERE grad_yr=9999;''')
conn.commit

cur.execute('''ALTER TABLE match_history_process ADD dropout int;''')
conn.commit

cur.execute('''UPDATE match_history_process SET dropout=1 WHERE match_closure_reason_super='Mentor can no longer participate';''')
conn.commit

cur.execute('''UPDATE match_history_process SET dropout=0 WHERE match_closure_reason_super!='Mentor can no longer participate';''')
conn.commit

cur.execute('''UPDATE match_history_process SET dropout=0 WHERE match_closure_reason_super IS NULL;''')
conn.commit	

cur.execute('''ALTER TABLE match_history_process ADD match_days int;''')
conn.commit

cur.execute('''UPDATE match_history_process SET match_days=length_of_match_in_days WHERE length_of_match_in_days >= 0;''')
conn.commit

cur.execute('''UPDATE match_history_process SET match_days=(date '2016-10-26' - match_start_date) WHERE length_of_match_in_days IS NULL;''')
conn.commit

cur.execute('''ALTER TABLE match_history_process ADD start_year int, end_year int;''')
conn.commit

cur.execute('''UPDATE match_history_process SET start_year=date_part('year',match_start_date;''')
conn.commit

cur.execute('''UPDATE match_history_process SET end_year=date_part('year',match_end_date;''')
conn.commit
	
conn.close()



