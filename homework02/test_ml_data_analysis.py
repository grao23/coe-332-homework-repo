from ml_data_analysis import mass_per_hemisphere
from ml_data_analysis import mass_per_hemisphere_longtitude

import pytest
import pandas as pd

# Tests For function mass_per_hemisphere(latitude)

testing_data = {'name': ["first", "second", "third"], 'reclat': [100.0, 50.0, -25.0], 
                'reclong': [30.0, -25.0, 100.0], 'mass (g)': [100, 200, 300]}


def test_mass_per_hemisphere(): 
    test_df = pd.DataFrame(testing_data)
    south,north = mass_per_hemisphere(test_df)

    assert south == 300.0
    assert north == 150.0
    assert isinstance(south, float)
    assert isinstance(north, float)


def test_mass_per_hemisphere_longtitude():
    test_df = pd.DataFrame(testing_data)
    east,west = mass_per_hemisphere(test_df)

    assert east == 200.0
    assert west == 200.0
    assert isinstance(east, float)
    assert isinstance(west, float)


def test_mass_per_hemisphere_exceptions():
    with pytest.raises(TypeError):
        mass_per_hemisphere(pd.DataFrame({'reclat': [0], 'mass (g)': ['invalid']}))
    
    with pytest.raises(KeyError):
        mass_per_hemisphere(pd.DataFrame({'mass (g)': [100]}))
    with pytest.raises(KeyError):
        mass_per_hemisphere(pd.DataFrame({'reclat': [0]}))


def test_mass_per_hemisphere_longtitude():
    with pytest.raises(TypeError):
        mass_per_hemisphere_longtitude(pd.DataFrame({'reclong': [0], 'mass (g)': ['invalid']}))                                                
    with pytest.raises(KeyError):
        mass_per_hemisphere_longtitude(pd.DataFrame({'mass (g)': [100]}))
    with pytest.raises(KeyError):
        mass_per_hemisphere_longtitude(pd.DataFrame({'reclong': [0]}))  












