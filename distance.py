#This function converts miles to kilometers and kilometers to miles
#by Sara Lytle

#miles to kilometers #insert miles into x

km2m = 0.621371
m2km = 1.60934

def miles_to_kilometers(x):
    """calculate miles to kilometers"""
    kilometers = m2km * x
    return kilometers

#kilometers to miles #insert kilometers into y

def kilometers_to_miles(y):
    """calculate kilometers to miles"""
    miles  = y * km2m
    return miles

