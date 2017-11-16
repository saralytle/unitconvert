import pytest

from unitconvert import distance

def test_distance_m2km():
    #known results
    assert miles_to_kilometers(1) == 1.60934

def test_distance_km2m():
    #KNOWN RESULTS
    assert kilometers_to_miles(1) == 0.621371

#from unitconvert import temperature

#def test_temperature():
    #known results
#assert temperature(0, 32)

with pytest.raises(TypeError):
    distance(1,2,3,4)

#with pytest.raises(TypeError):
#temperature(1,2,3,4)


