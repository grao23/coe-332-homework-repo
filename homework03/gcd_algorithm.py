import math 
import pandas as pd
import logging

logging.basicConfig()

df = pd.read_csv("Meteorite_Landings.csv")

df['mass (g)'] = pd.to_numeric(df['mass (g)'], errors = "coerce")
df['reclat'] = pd.to_numeric(df['reclat'], errors = "coerce")
df['reclong'] = pd.to_numeric(df['reclong'], errors = "coerce")



def circle(latitute1:float, longtitude1:float, latitude2:float, longtitude2:float) -> float:
    ''' 
    This function outputs the distance between 2 asteroids based on where they have landed. 

    Arguments: 
    latitude1: the latitude of the first asteroid
    longtitude1: the longtitude of the first asteroid
    latitude2: the latitude of the second asteroid
    longtitude1: the longtitude of the second asteroid

    Returns: 
    It returns D which is the distance in km between the two asteroids

    
    '''
    r = 6371

    latitude1, longtitude1,latitude2,longtitude2 = map(math.radians, [latitute1, longtitude1,latitude2,longtitude2])

    #Difference in Latitude and Longitude
    
    differnce_latitude = latitude2 - latitude1
    difference_longtitude = longtitude2 - longtitude1

    a = math.acos((math.sin(latitude1)*math.sin(latitude2)) + math.cos(latitude1)*math.cos(latitude2) * math.cos(difference_longtitude))
    d = r * a

    return d



