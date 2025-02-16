##HOMEWORK 3


The goal of this directory is to show how to write a Dockerfile which can containerize the files which we have made from the previous homework assignement. 


----Neccessary Data and where to find it

The data can be found and uploaded to your directory using this code line: wget https://raw.githubusercontent.com/TACC/coe-332-sp25/main/docs/unit02/sample-data/Meteorite_Landings.json
Then use this code to convert your file into a csv file:
import csv
import json

data = {}

with open('Meteorite_Landings.json', 'r') as f:
    data = json.load(f)

with open('Meteorite_Landings.csv', 'w') as o:
    csv_dict_writer = csv.DictWriter(o, data['meteorite_landings'][0].keys())
    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(data['meteorite_landings'])


To build our image: 

docker build -t <gautamrao>/<ml_data_analysis>:1.0 ./


To mount data at runtime: 

docker run -v $(pwd)/ml_data_analysis.py:/code/ml_data_analysis.py \ (do this for each file can be done together as well) 

To run code: 

docker run -v $(pwd)/ml_data_analysis.py:/code/ml_data_analysis.py \ dockerfile python /code/ml_data_analysis.py



----File Descriptions:

Dockerfile --> This file goal is containerize the contents of the files below. We first use the FROM function to take the python 3.12 environment and then we start installing our dependecies in Pandas 
and Pytest using the RUN function. Following this we copy the files from below by using the COPY function to be able to copy them into our data container which we want to run later. Following this we use 
the RUN function once more to run each file individually inside of the container. 

ml_data_analysis --> This files goal is to print out certain summary data statitics related to the code which we have written. In the code we will see 3 main functions which calcuate the average mass
of an meteorite in the north/south hemisphere, the average mass of a meteorite in the east/west hemisphere and the great circle algorithm which is imported from a seperate gcd_algorithm.py file.

gcd_algorithm --> This files goal is provide the written code which correlates to the great circle algorithm equation. I used data provided on the homework02 website page to get the value of R = 6371 as 
well as getting the equation which we then multiplied by the R value to get the distance between 2 meteorites in kilometers(km). 

test_ml_data_analysis --> This file is used to see if the code written by me can be used to pass multiple test cases and see the strength of our code. I used a fake set of data which corresponded to a
meteor having a specific latitude, longitude and mass (g). From there I imported the functions mass_per_hemisphere and mass_per_hemisphere_longtitude and inputted this data. I used the "assert" function 
to then determine if the output of the code will be exactly what I want it to be. If it is true it passes the test, and if false the test failes. I also included "pytest.raises" errors to test if there 
are any errors within the data, if there is it should raise that error. 

test_gcd_algorithm --> This files goal is to see if the great_circle_algorithm written can calculate the distance between known locations. In this file I used the example of Austin to Dallas. I first 
imported the "circle" function from the gcd_algorithm.py file, and then searched up online the latitude and longitude of Dallas and Austin and placed them under certain variables. Following this I 
placed those cooridnates into the "circle" function and used the assert function to check if the distance is between 290 and 300 km(The distsance between Dallas and Austin is 296.66 according to Google). 
I also included "pytest.raises" errors to test if there are any errors within the data, if there is it should raise that error.
