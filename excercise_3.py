units = input("SELECT USC OR METRIC AS YOUR UNIT CHOICE; (SELECT 'METRIC' or 'USC')") #Create an input statement to let the user select what they want
distance = float(input("How far did you travel?")) #create an input statement for distance
fuel = float(input("How Much gas did you use?")) #do the same for gas usage
d = distance/fuel #calculate fuel usage
if (units == "USC"):
    the_distance = (distance, "miles")
    the_fuel = (fuel, "gallons")
    the_fuel_consumption = (d, "mpg")
    the_distance_convert = (the_distance * 1.60934, "km")
    the_fuel_convert = (the_fuel * 3.78541, "Liters")
    rating = the_fuel_consumption * (62.1371/.264172)
    the_fuel_consumption_convert = (the_fuel_consumption * (62.1371/.264172), "Liters/1OOkm")
    if (rating > 20):
        fuel_rating = ("Extremely Poor")
    elif (rating > 15 and rating <= 20):
        fuel_rating = ("Poor")
    elif (rating > 10 and rating <= 15):
        fuel_rating = ("Average")
    elif (rating > 8 and rating <= 10):
        fuel_rating =  ("Good")
    elif (rating <= 8):
        fuel_rating = ("Excellent")
else:
    if (units == "METRIC"):
        the_distance = (distance, "kilometers")
        the_fuel = (fuel, "Liters")
        the_fuel_consumption = (d * 100, "Liters/100Km")
        the_distance_convert = (the_distance / 1.60934, "Miles")
        the_fuel_convert = (the_fuel * 3.78541, "Gallons")
        rating = the_fuel_consumption
        the_fuel_consumption_convert = (the_fuel_consumption * (62.1371 / .264172), "mpg")
        if (rating > 20):
            fuel_rating = ("Extremely Poor")
        elif (rating > 15 and rating <= 20):
            fuel_rating = ("Poor")
        elif (rating > 10 and rating <= 15):
            fuel_rating = ("Average")
        elif (rating > 8 and rating <= 10):
            fuel_rating = ("Good")
        elif (rating <= 8):
            fuel_rating = ("Excellent")






