import pandas as pd 
import logging

logging.basicConfig()

df = pd.read_csv("Meteorite_Landings.csv")

df['mass (g)'] = pd.to_numeric(df['mass (g)'], errors = "coerce")
df['reclat'] = pd.to_numeric(df['reclat'], errors = "coerce")
df['reclong'] = pd.to_numeric(df['reclong'], errors = "coerce")


#Measures the average mass of an asteroid in an hemisphere"
def mass_per_hemisphere(df:pd.DataFrame) -> tuple:
    '''
    This function is used to calculate the average mass of an asteroid which falls in the northern or southern hemisphere

    Arguments: 
    df: Is the dataframe which we have read in from the Meteorite_Landings.csv file

    Returns: 

    It returns the average mass of a asteroid in the northern hemisphere and southern hemisphereas seperate values

    '''
    mass_in_north = df[df['reclat'] > 0]['mass (g)']
    mass_in_south = df[df['reclat'] <= 0]['mass (g)']


    average_mass_in_north = mass_in_north.mean()
    average_mass_in_south = mass_in_south.mean()

    return average_mass_in_south, average_mass_in_north


mass_south, mass_north = mass_per_hemisphere(df)

print(f"Avg mass in South: {mass_south}")
print(f"Avg mass in North: {mass_north}")

#Measures the average mass of an asteroid in the east and west hemisphere

#Measures the average mass of an asteroid in an hemisphere"
def mass_per_hemisphere_longtitude(df:pd.DataFrame) -> tuple:
    '''
    This function is used to calculate the average mass of an asteroid which falls in the eastern or western hemisphere

    Arguments:
    df: Is the dataframe which we have read in from the Meteorite_Landings.csv file

    Returns:

    It returns the average mass of a asteroid in the eastern hemisphere and western hemisphereas seperate values

    '''
    mass_in_east = df[df['reclong'] > 0]['mass (g)']
    mass_in_west = df[df['reclong'] <= 0]['mass (g)']


    average_mass_in_east = mass_in_east.mean()
    average_mass_in_west = mass_in_west.mean()

    return average_mass_in_east, average_mass_in_west



mass_east, mass_west = mass_per_hemisphere_longtitude(df)


print(f"Avg mass in East: {mass_east}")
print(f"Avg mass in West: {mass_west}")


#Function 3  the GCD algorithm 

from gcd_algorithm import circle

#run output for it

print(circle(df["reclat"][0], df["reclong"][0], df["reclat"][1], df["reclong"][1]))


