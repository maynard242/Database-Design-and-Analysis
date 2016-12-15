README.txt Updated Dec 15, 2016

Collection of programs in python3 to read and process data

TO LOAD RAW data

post_load_match_history.py 				- Loads match history data
post_load_mentor_demo_table.py		- Loads mentor demographic data
post_load_mentor_behavior.py			- Loads mentor platform behavior data
post_load_platform_behavior.py		- Loads platform behavior data
post_load_mentee_behavior.py			- Loads mentee platform behavior data
post_load_master_table.py					- Loads master table data

THE FOLLOWING TABLES WILL BE CREATED IN PROGRESS AFTER ABOVE PROGRAMS ARE RUN

match_history
mentor_demo
mentor_behavior
platform_behavior
mentee_behavior
master_table

TO PROCESS data

post_process_match_history.py				- Process data in match_history (cleaning and transformation, including new variables)
post_process_mentor_demo.py					- Process data in mentor_demo table
post_process_master_table.py				- Process data in master_table table

THE FOLLOWING PROCESSED TABLES ARE CREATED

match_history_process
mentor_demo_process
master_table_process

FINAL TABLES ARE CREATED WITH THE FOLLOWING PROGRAMS

post_create_tables.py								- Create final TABLES

FINAL TABLES CREATED

t1_mentor_behavior
t2_mentee_behavior
t3_match_history
t4_demography
t5_imentor_master1516
t6_zipcodes


