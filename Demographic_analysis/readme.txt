### PREDICTIVE ANALYTICS PROGRAM ###

### STEP-BY-STEP INSTRUCTIONS ON HOW TO RUN THE PROGRAM ###

USAGE:
This program is to run different predictive analysis algorithms and produce results in a csv file.


INSTRUCTION STEPS:

STEP 1 - Environment and Tool Setup

1. Program:
This program is written in Python 2.7. Please ensure the correct version of Python 2.7 is properly installed and running the program. The program codes are within the web application Jupyter notebook.

2. Python libraries:
a) Install psycorpg2 (Python library for interacting with Postgres) by running from terminal window:
	$ pip install psycopg2

	or in case of the Anaconda package is used, then use the conda package management:
	$ conda install psycopg2

b) Other libraries
Make sure that these libraries and packages are installed:
numpy
pandas
matplotlib
scipy
sklearn
seaborn
time
pydotplus


STEP 2 -  Application setup

1. Pull the iPython notebook from the Git Hub repository: 
https://github.com/maynard242/W205ProjectAwesome/tree/master/Demographic_analysis

1. In terminal window, change directory to the directory in which the notebook is saved and start the iPython notebook by running:	$ jupyter notebook

2. In the web application, select demographics-without-match-length-Dec13.ipynb.


STEP 3 - Application deployment

1. Once in the selected notebook, run each cell. Please read the instructions for each cell, if any. Also, 4 images of the decision trees will also be created and saved in the same directory as the notebook directory.

2. Once all cells are run, a CSV file containing prediction results will be created. Load this file to the Tableau tool that is connected to the Postgres database to visualize the results.


