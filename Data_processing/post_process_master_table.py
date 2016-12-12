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

cur.execute('''ALTER TABLE master_table_process ADD touchpoints INT,
																								ADD mentor_online_freq INT,
																								ADD pair_online_freq INT,
																								ADD pair_meetings INT
																								ADD x1 INT
																								ADD x2 INT
																								ADD x3 INT
																								ADD x4 INT
																								ADD x5 INT
																								ADD x6 INT
																								ADD x7 INT
																								ADD x8 INT;''')
conn.commit()

# Creatting touchpoints

cur.execute('''UPDATE master_table_process SET touchpoints= ROUND((mentor_tp_1314 + mentor_tp_1415 + mentor_tp_1516),0);''')
conn.commit()

# Creating overall mentor_online_freq

cur.execute('''UPDATE master_table_process SET x1=0 WHERE mentor_online_freq_1213=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x1=1 WHERE mentor_online_freq_1213!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=0 WHERE mentor_online_freq_1415=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=1 WHERE mentor_online_freq_1415!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=0 WHERE mentor_online_freq_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=1 WHERE mentor_online_freq_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=0 WHERE mentor_online_freq_1213=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=mentor_online_freq_1213 WHERE mentor_online_freq_1213!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=0 WHERE mentor_online_freq_1415=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=mentor_online_freq_1415 WHERE mentor_online_freq_1415!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x6=0 WHERE mentor_online_freq_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x6=mentor_online_freq_1516 WHERE mentor_online_freq_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET mentor_online_freq= ROUND( (x4+x5+x6) /(x1+x2+x3),0 );''')
conn.commit()

# Creating pair_online_freq

cur.execute('''UPDATE master_table_process SET x1=0 WHERE pair_online_freq_1213=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x1=1 WHERE pair_online_freq_1213!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=0 WHERE pair_online_freq_1314_A=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=1 WHERE pair_online_freq_1314_A!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=0 WHERE pair_online_freq_1415=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=1 WHERE pair_online_freq_1415!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=0 WHERE pair_online_freq_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=1 WHERE pair_online_freq_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=0 WHERE pair_online_freq_1213=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=pair_online_freq_1213 WHERE pair_online_freq_1213!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x6=0 WHERE pair_online_freq_1314_A=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x6=pair_online_freq_1314_A WHERE pair_online_freq_1314_A!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x7=0 WHERE mentor_online_freq_1415=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x7=pair_online_freq_1415 WHERE pair_online_freq_1415!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x8=0 WHERE pair_online_freq_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x8=pair_online_freq_1516 WHERE pair_online_freq_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET pair_online_freq= ROUND( (x5+x6+x7+x8) /(x1+x2+x3+x4),0 );''')
conn.commit()

# Creating pair_meetings

cur.execute('''UPDATE master_table_process SET x1=0 WHERE pair_meetings_1213=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x1=pair_meetings_1213 WHERE pair_meetings_1213!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=0 WHERE pair_meetings_1314_A=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x2=pair_meetings_1314_A WHERE pair_meetings_1314_A!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=0 WHERE pair_total_mtgs_1415=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x3=pair_total_mtgs_1415 WHERE pair_total_mtgs_1415!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=0 WHERE pair_curriculum_mtgs_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x4=pair_curriculum_mtgs_1516 WHERE pair_curriculum_mtgs_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=0 WHERE pair_other_mtgs_1516=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET x5=pair_other_mtgs_1516 WHERE pair_other_mtgs_1516!=9999;''')
conn.commit()

cur.execute('''UPDATE master_table_process SET pair_meetings= ROUND( x1+x2+x3+x4+x5,0 );''')
conn.commit()

cur.execute('''ALTER TABLE master_table_process DROP x1 INT
																								DROP x2 INT
																								DROP x3 INT
																								DROP x4 INT
																								DROP x5 INT
																								DROP x6 INT
																								DROP x7 INT
																								DROP x8 INT;''')
conn.close()


