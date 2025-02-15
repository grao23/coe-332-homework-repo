from gcd_algorithm import circle 

import pytest
import pandas as pd 


def test_circle():

    '''
    
    This function is used as a test function to test if the circle function can output the distance between 2 places accurately

    Arguments:

    It takes none in intitally but in the function we define austin_latitude, austin_longtitude, dallas_latitude, dallas_longtitude to then use it in our circle function

    Returns:

    This returns a pass or fail as we are using an assert function to check if it is between the values 290 and 300 (which it is)
    

    '''
    # Test same point (should return 0)
    assert round(circle(0, 0, 0, 0), 6) == 0

    ausitn_latitude, austin_longitude = 30.2672, -97.7431
    dallas_latitude, dallas_longitude= 32.7767, -96.7970
    assert 290 < circle(ausitn_latitude, austin_longitude, dallas_latitude, dallas_longitude) < 300



    assert isinstance(circle(0, 0, 1, 1), float)

def test_circle_exceptions():
    with pytest.raises(TypeError):
        circle("a", 0, 0, 0)
    with pytest.raises(TypeError):
        circle(0, "b", 0, 0)
    with pytest.raises(TypeError):
        circle(0, 0, "c", 0)
    with pytest.raises(TypeError):
        circle(0, 0, 0, "d")
