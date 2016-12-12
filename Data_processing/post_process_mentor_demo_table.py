#/usr/bin/env python3

# Program to do some processing of the mentor_demo table (new -> mentor_demo_process)

import psycopg2

conn = psycopg2.connect(database="awesome", user = "awesome_admin",
password="w205.Awesome", host = "34.193.7.196", port="5432")
    
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS mentor_persona AS SELECT mentor_persona_id FROM match_history_process;''' )
conn.commit()

cur.execute('''CREATE TABLE IF NOT EXISTS mentor_demo_tmp AS 
SELECT 
	mentor_demo.mentor_persona_id,
	mentor_user_id,
	Racial_Group,
	Gender,
	Application_Source,
	Birthdate,
	Lives_in_Borough,
	Current_Career,
	Date_Matched,
	Date_Match_End,
	Have_Children, 
	Current_Occcupation,
	Marital_Status,
	Level_of_Education,
	Partner_Site,
	School_cohort_id,
	program_type,
	Mailing_Zip_PostalCode,
	Language_other_than_English,
	Parent_Guardian_College_Degree,
	College_Majors,
	How_did_you_hear_about_iMentor,
 	Employer,
	Colleges_Attended 
FROM mentor_demo
JOIN mentor_persona
ON mentor_demo.mentor_persona_id=mentor_persona.mentor_persona_id;''')	
conn.commit()
	
cur.execute('''CREATE TABLE IF NOT EXISTS mentor_demo_process AS
	SELECT 
	match_history_process.match_start_date,
	mentor_demo_tmp.mentor_persona_id,
	mentor_demo_tmp.mentor_user_id,
	mentor_demo_tmp.Racial_Group,
	mentor_demo_tmp.Gender,
	mentor_demo_tmp.Application_Source,
	mentor_demo_tmp.Birthdate,
	mentor_demo_tmp.Lives_in_Borough,
	mentor_demo_tmp.Current_Career,
	mentor_demo_tmp.Date_Matched,
	mentor_demo_tmp.Date_Match_End,
	mentor_demo_tmp.Have_Children, 
	mentor_demo_tmp.Current_Occcupation,
	mentor_demo_tmp.Marital_Status,
	mentor_demo_tmp.Level_of_Education,
	mentor_demo_tmp.Partner_Site,
	mentor_demo_tmp.School_cohort_id,
	mentor_demo_tmp.program_type,
	mentor_demo_tmp.Mailing_Zip_PostalCode,
	mentor_demo_tmp.Language_other_than_English,
	mentor_demo_tmp.Parent_Guardian_College_Degree,
	mentor_demo_tmp.College_Majors,
	mentor_demo_tmp.How_did_you_hear_about_iMentor,
 	mentor_demo_tmp.Employer,
	mentor_demo_tmp.Colleges_Attended
	FROM match_history_process
	JOIN mentor_demo_tmp
	ON mentor_demo_tmp.mentor_persona_id=match_history_process.mentor_persona_id;''')	
conn.commit()
	
cur.execute('''DROP TABLE mentor_persona;''' )
conn.commit()

cur.execute('''DROP TABLE mentor_demo_tmp;''' )
conn.commit()

cur.execute('''ALTER TABLE mentor_demo_process ADD hear_about_imentor TEXT;''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='Not available' WHERE How_did_you_hear_about_iMentor IS NULL OR How_did_you_hear_about_iMentor='N/A' OR How_did_you_hear_about_iMentor='0';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='alumni' WHERE How_did_you_hear_about_iMentor='Alumni / University Network' OR How_did_you_hear_about_iMentor='Alumni Group' OR How_did_you_hear_about_iMentor='Alumni Network';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='employer' WHERE How_did_you_hear_about_iMentor='Co-worker' OR How_did_you_hear_about_iMentor='Co-worker / Employer' OR How_did_you_hear_about_iMentor='Community Group/Network' OR How_did_you_hear_about_iMentor='Coworker' OR How_did_you_hear_about_iMentor='Employer';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='socialmedia' WHERE How_did_you_hear_about_iMentor='Facebook' OR How_did_you_hear_about_iMentor='LinkedIn' OR How_did_you_hear_about_iMentor='Social Media (Twitter, Instagram, etc.)' OR How_did_you_hear_about_iMentor='Twitter';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='friendfamily' WHERE How_did_you_hear_about_iMentor='Family / Friend' OR How_did_you_hear_about_iMentor='Friend / Family' OR How_did_you_hear_about_iMentor='Friend/Family' OR How_did_you_hear_about_iMentor='Friend/Family; Employer' OR How_did_you_hear_about_iMentor='Friend/Family; Friend/Family';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='volunteerwebsite' WHERE How_did_you_hear_about_iMentor='Idealist' OR How_did_you_hear_about_iMentor='Mentoring.org' OR How_did_you_hear_about_iMentor='Mentoring.org; Friend/Family' OR How_did_you_hear_about_iMentor='NYCService' OR How_did_you_hear_about_iMentor='Volunteer Fair' OR How_did_you_hear_about_iMentor='Volunteer Website' OR How_did_you_hear_about_iMentor='Website (Idealist, NYC Service, etc.)';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='other' WHERE How_did_you_hear_about_iMentor='I have not seen an iMentor ad.' OR How_did_you_hear_about_iMentor='My home aNot ddress' OR How_did_you_hear_about_iMentor='News Article' OR How_did_you_hear_about_iMentor='Online Ad' OR How_did_you_hear_about_iMentor='Other' OR How_did_you_hear_about_iMentor='Subway' OR How_did_you_hear_about_iMentor='TV Ad' OR How_did_you_hear_about_iMentor='University';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='web' WHERE How_did_you_hear_about_iMentor='Surfing the Web';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET hear_about_imentor='nominated' WHERE How_did_you_hear_about_iMentor='Nomination / Mentor Together Email' OR How_did_you_hear_about_iMentor='Nomination Email';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Not available' WHERE Current_Career='N/A' OR Current_Career='I do not know or prefer not to answer' OR Current_Career='N/A-Does not apply to my situation' OR Current_Career='None' OR Current_Career='0' OR Current_Career='' OR Current_Career IS NULL;''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Achitecture' WHERE Current_Career='Architecture & Planning';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Arts' WHERE Current_Career='Arts & Entertainment';''')
conn.commit()
	
cur.execute('''UPDATE mentor_demo_process SET current_career='Communications' WHERE Current_Career='Communications' OR Current_Career='Communications, Technology';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Computer' WHERE Current_Career='Computer Programmer | Computer Software Engineer';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Finance' WHERE Current_Career='Finance | Investor / Stockbroker';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Law' WHERE Current_Career='Law & Public Policy';''')
conn.commit()	

cur.execute('''UPDATE mentor_demo_process SET current_career='Non-Profit' WHERE Current_Career='Non-Profit & Social Services';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET current_career='Trades' WHERE Current_Career='Trades / Vocations';''')
conn.commit()	

cur.execute('''UPDATE mentor_demo_process SET level_of_education='Not available' WHERE level_of_education='N/A' OR level_of_education='None' OR level_of_education='0' OR level_of_education='' OR level_of_education IS NULL;''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET level_of_education='2-Year college' WHERE level_of_education='2-Year college degree (Associate''s)' OR level_of_education='2-Year college degree (Associate''s), 4-Y' OR level_of_education='High School Diploma, 2-Year college degr';''')
conn.commit()
	
cur.execute('''UPDATE mentor_demo_process SET level_of_education='4-Year College' WHERE level_of_education='4-Year College Degree (Bachelor''s)' OR level_of_education='4-Year College Degree (Bachelor''s), 2-Ye' OR level_of_education='4-Year College Degree (Bachelor''s), Mast' OR level_of_education='4-Year College Degree (Bachelor''s); High School Diploma' OR level_of_education='4-Year College Degree (Bachelor''s); High School Diploma, 4-Year College Degr' OR level_of_education='High School Diploma, 4-Year College Degr' OR level_of_education='Dartmouth College';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET level_of_education='High School' WHERE level_of_education='High School Diploma';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET level_of_education='Master''s Degree' WHERE level_of_education='High School Diploma, Master''s Degree' OR level_of_education='High School Diploma, Master''s Degree, 4-' OR level_of_education='Master''s Degree (MBA, MPA, MA, etc.)';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET level_of_education='PhD' WHERE level_of_education='High School Diploma, Master''s Degree, Ph' OR level_of_education='High School Diploma, PhD or other advanc' OR level_of_education='PhD or other advanced degree (Law, Medic' OR level_of_education='PhD, JD, or MD';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET racial_group='Not specified' WHERE racial_group='N/A' OR racial_group='None' OR racial_group='0' OR racial_group='' OR racial_group IS NULL OR racial_group='I identify with a race not listed here' OR racial_group='I would prefer not to indicate my ethnic' OR racial_group='I would prefer not to indicate my race' OR racial_group='Not Specified' OR racial_group='Not Specified, Other' OR racial_group='Other';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET racial_group='Asian / Pacific Islander' WHERE racial_group='Asian / Pacific Islander' OR racial_group='Asian / Pacific Islander | Black / Afric' OR racial_group='Asian / Pacific Islander | Hispanic (May' OR racial_group='Asian / Pacific Islander | I identify wi' OR racial_group='Asian / Pacific Islander | White (Non-Hi' OR racial_group='Asian / Pacific Islander | White (Non-Hispanic)' OR racial_group='Asian / Pacific Islander, Black / Africa' OR racial_group='Asian / Pacific Islander, Hispanic (May' OR racial_group='Asian / Pacific Islander, Other' OR racial_group='Asian / Pacific Islander, Other, White (' OR racial_group='Asian / Pacific Islander, White (Non-His' OR racial_group='Asian/Pacific Islander';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET racial_group='Black / African American' WHERE racial_group='Black / African American' OR racial_group='Black / African American | Hispanic (May' OR racial_group='Black / African American | I identify wi' OR racial_group='Black / African American | I identify with a race not listed here' OR racial_group='Black / African American | White (Non-Hi' OR racial_group='Black / African American, Hispanic (May' OR racial_group='Black / African American, Other' OR racial_group='Black / African American, Other, White (' OR racial_group='Black / African American, White (Non-His' OR racial_group='Black/African American';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET racial_group='Hispanic' WHERE racial_group='Hispanic (May be of any race)' OR racial_group='Hispanic (May be of any race) | Native A' OR racial_group='Hispanic (May be of any race) | White (N' OR racial_group='Hispanic (May be of any race) | White (Non-Hispanic)' OR racial_group='Hispanic (May be of any race), Other' OR racial_group='Hispanic (May be of any race), White (No';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET racial_group='White (Non-Hispanic)' WHERE racial_group='Other, White (Non-Hispanic)' OR racial_group='White (Non-Hispanic)' OR racial_group='White (Non-Hispanic) | I identify with a' OR racial_group='White (Non-Hispanic); Asian / Pacific Islander' OR racial_group='White (Non-Hispanic); I identify with a race not listed here';''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET Current_Occcupation='Not available' WHERE Current_Occcupation='N/A' OR Current_Occcupation='None' OR Current_Occcupation='0' OR Current_Occcupation='' OR Current_Occcupation IS NULL;''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET Current_Occcupation='Lawyer' WHERE Current_Occcupation LIKE '%Lawyer%';''')
conn.commit()

######### Recheck

cur.execute('''ALTER TABLE mentor_demo_process ADD age_at_match INT;''')
conn.commit()

cur.execute('''UPDATE mentor_demo_process SET age_at_match = (match_start_date- birthdate);''')
conn.commit

conn.close()


