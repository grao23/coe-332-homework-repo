import math 
import pandas as pd

df = pd.read_csv("Meteorite_Landings.csv")

df['mass (g)'] = pd.to_numeric(df['mass (g)'], errors = "coerce")
df['reclat'] = pd.to_numeric(df['reclat'], errors = "coerce")
df['reclong'] = pd.to_numeric(df['reclong'], errors = "coerce")



def circle(latitute1:float, longtitude1:float, latitude2:float, longtitude2:float) -> float:
    r = 6371

    latitude1, longtitude1,latitude2,longtitude2 = map(math.radians, [latitute1, longtitude1,latitude2,longtitude2])

    #Difference in Latitude and Longitude
    
    differnce_latitude = latitude2 - latitude1
    difference_longtitude = longtitude2 - longtitude1

    a = math.acos((math.sin(latitude1)*math.sin(latitude2)) + math.cos(latitude1)*math.cos(latitude2) * math.cos(difference_longtitude))
    d = r * a

    return d



