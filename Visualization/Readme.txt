### Visualizations in Tableau ###

### VIEW DASHBOARDS ###
URL: https://10az.online.tableau.com/t/ucbsfan/views/MentorAnalysis/MentorDropoutDashboard?:embed=y&:showShareOptions=false&:display_count=no&:showVizHome=no

Visualizations will only be viewable at the above URL until 12/17/16.
Contact stephanie.fan@ischool.berkeley.edu to add users.

### STEP-BY-STEP INSTRUCTIONS ON HOW TO RUN/UPDATE THE TABLEAU ###

USAGE:
This program is to create dashboards from the database and analysis.


INSTRUCTION STEPS:

1. Program: Tableau

2. Dependencies:
Run the following code from Github repository before starting. Refer to the readme.txt in each folder for more details on how to run.
a) Data_processing
b) Demographic_analysis

Ensure that the prediction_actives_dropout proba.csv output for the mentor dropout probability (generated as part of running Demographic_analysis is downloaded.

3. Open the file and re-connect data sources
a) Install Postgres driver if not already installed (https://www.tableau.com/support/drivers)
b) Open the Visualizations.twb file
c) You may be prompted for credentials and files. 
    Enter login information for the Postgres database (this may be different if running on a new server). Defaults are below:
      server: 34.193.7.196
      port: 5432
      user: awesome_admin
      pw: w205.Awesome
    If prompted, locate the  the prediction_actives_dropout proba.csv file on the local drive. You can load the most updated file by going to the Data Sources tab, and editing the prediction_actives_dropout proba.csv connection.

4. Make new graphs and/or enjoy existing visualizations!
