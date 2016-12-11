#/usr/bin/env python3

# Program to do some processing of the master-table (new -> master_table_process)

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS master_table_process AS SELECT * FROM master_table;''')	
conn.commit()

cur.execute('''ALTER TABLE master_table_process ADD same_eth_mentee INT;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET same_eth_mentee=1 WHERE mentee_eth=mentor_eth AND mentor_eth !=0 AND mentee_eth != 0;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET same_eth_mentee=0 WHERE mentee_eth != mentor_eth;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET same_eth_mentee=0 WHERE mentor_eth IS NULL OR mentee_eth IS NULL;''')
conn.commit()

## To do if needed mentor_online_freq
#pair_online_freq
#touchpoints
#pair_meetings

cur.execute('''ALTER TABLE master_table_process ADD pair_online_freq FLOAT;''')
conn.commit()

cur.execute('''ALTER TABLE master_table_process ADD touchpoints FLOAT;''')
conn.commit()

cur.execute('''ALTER TABLE master_table_process ADD pair_meetings FLOAT;''')
conn.commit()

conn.close()


