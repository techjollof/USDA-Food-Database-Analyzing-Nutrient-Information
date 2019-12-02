# USDA Food Database-Analyzing Nutrient Information



Necessary instructions for the end-user to install the required files and run this project:

?	This program lets you analyse Food and nutrient information is available on the US Department of Agriculture website. However, the formatting leaves a lot to be desired and we would like use data in JSON format to proceed further.

The first section of this program was done in python 2 
?	which can be download here https://www.python.org/download/releases/
?	Download nutrient-db python utility from GitHub from https://github.com/schirinos/nutrient-db.git
?	To generate an SQLite database file from the flat files included in the repo run: python nutrientdb.py
?	Run the main program with python nutrientdb.py -e > nutrients.json to convert the USDA data to JSON format. For further details, check https://github.com/schirinos/nutrient-db. You might have to install the python utility for MongoDB interface via pip install pymongo

Second section of the program is in python 3
?	This program was written in Python 3. thus requires the installation of it which can be download here https://www.python.org/download/releases/
?	Small dataset used in the program can be downloaded from 
?	You should be able to run this code on any platform. 
?	A number of external libraries have been used in this project including ¨C numpy, scipy, matplotlib, pandas which can be install by using pip install package name
?	The code was created using Spyder on Anaconda. The user should be able to run this through any python 3 platform. Ideally, launching from the command-line interpreter has not been tested. 


