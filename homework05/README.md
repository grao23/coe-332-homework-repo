##HOMEWORK 5


Title: SUMMARY STATITICS FOR ISS DATA


Description for folder: 

This folder's goal is to provide different summary statistics for ISS data written on a containerized Python script which is stored on as a public 
dataset on NASA's website. It is ISS data for a 15 day period. Its important that we are able to decipher this data as it can be used for tracking
the movement of the ISS and seeing exactly what speed its travelling at and which direction it is headed in. 



How to Access data: 

I used the requests library to load the data into my file. The code to do this is as follows:

import requests

response = requests.get(url='https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')

I also used the wget https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml feature outside the script in the 
termial to play around with the data and see some of the features I am working with. 

Inside of the "stateVector" column in the xml file it contained the "X,Y,Z, X_DOT, Y_DOT, Z_DOT, EPOCH" features which is the data we want to work 
with. 


How to build container for code: 

I used nano to create a Dockerfile to containerize the Python3 code which I had made, I had done it with the following code snippet, in which I 
loaded python 3.12, then installed the required libraries (pytest, math, xmltodict, flask, requests) and then used the COPY and RUN functions to load the scripts 
into the file. 

CODE to containerize Flask: 

FROM python:3.12

RUN pip3 install xmltodict
RUN pip3 install datetime
RUN pip3 install pandas
RUN pip3 install pytest==8.3.4
RUN pip3 install flask
RUN pip3 install requests


RUN mkdir /app
WORKDIR /app


COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


COPY iss_tracker.py /app/iss_tracker.py
COPY test_iss_tracker.py /app/test_iss_tracker.py



RUN chmod +rx /app/iss_tracker.py
RUN chmod +rx /app/test_iss_tracker.py



ENV PATH="/app:$PATH"


ENTRYPOINT ["python"]

CMD ["iss_tracker.py"]
CMD ["test_iss_tracker.py"]


How to run the containerized scripts: 


use this to get to devolopment environment:

docker run --rm -it -v $PWD/ gautamrao/iss_tracker.py:1.0 /bin/bash

docker run --rm -it -v $PWD/ gautamrao/test_iss_tracker.py:1.0 /bin/bash



Expected output: 

The expected output for the iss_tracker.py file should be of the 3 main functions which are present in the code: 

For the first function "date_range" the output would be a single line which contains the range of the dates which are present in the dataset. 

For the second function "closest_epoch" the ouptut contains 7 lines in which outputs the closest epach and the "X,Y,Z, X_DOT, Y_DOT, Z_DOT" 
associated with it.

For the third function "average_speed" the output is 2 lines, one which contains the average speed of the entire dataset, and the second line which 
has the instatenous speed. 


For the test_iss_tracker.py file the expected output includes the program passing a series of 6 test passes which should all be passed. 
