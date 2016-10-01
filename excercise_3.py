units = input("SELECT USC OR METRIC AS YOUR UNIT CHOICE; (TYPE 'METRIC' or 'USC', using double quotes and in all caps)") #Create an input statement to let the user select what they want
distance = float(input("How far did you travel?")) #create an input statement for distance
fuel = float(input("How Much gas did you use?")) #do the same for gas usage
d = (distance / fuel) #calculate fuel usage
if (units == "USC"): #setup a conditional statement if the user selects USC
    the_distance = (distance, "miles") #because we cant have a string in our other calculations involving distance; it's best to setup another variable with a string for the units
    the_fuel = (fuel, "gallons") #do the same as above for fuel (setup a separate variable with a string describing the number)
    the_fuel_consumption = (d, "mpg") #do the same as above for fuel consumption (setup a separate variable with a string describing the number)
    the_distance_convert = (distance * 1.60934) #convert the distance using the initial variable to kilometers
    the_fuel_convert = (fuel * 3.78541) #convert the fuel to liters using the initial variable
    the_fuel_consumption_convert = ((1/d) * (19.601)) #we need to to convert the fuel consumption from USC to METRIC
    rating = (1/d) * 19.601 # establish the fuel rating (must be in terms of kilometers; can't use previous variable because it has a string)
    if (rating > 20): #setup an if statement for the fuel rating; following the ranges from the table; do this using if and elif statements
        fuel_rating = ("Extremely Poor")
    elif (rating > 15 and rating <= 20):
        fuel_rating = ("Poor")
    elif (rating > 10 and rating <= 15):
        fuel_rating = ("Average")
    elif (rating > 8 and rating <= 10):
        fuel_rating =  ("Good")
    elif (rating <= 8):
        fuel_rating = ("Excellent")
    print 'Distance:', format(distance, '10.3f'), 'miles', format(the_distance_convert, '10.3f'), 'km'
    print "Gas:", format(fuel, '13.3f'), 'gallons', format(the_fuel_convert, '13.3f'), 'liters'
    print "Consumption:", format(d, '10.3f'), 'mpg', format(the_fuel_consumption_convert, '10.3f'), 'L/100km'
    print "gas consumption rating:", fuel_rating


else:
    if (units == "METRIC"):
        the_distance = (distance, "kilometers")
        the_fuel = (fuel, "Liters")
        the_fuel_consumption = (d * 100, "Liters/100Km")
        the_distance_convert = (distance * 1.60934)
        the_fuel_convert = fuel * 3.78541
        the_fuel_consumption_convert = (the_distance_convert / the_fuel_convert)
        rating = the_fuel_consumption
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
    print 'Distance:',format(distance, '10.3f'), 'Km', format(the_distance_convert,'10.3f'), 'Miles'
    print "Gas:", format(fuel, '13.3f'), 'Liters', format(the_fuel_convert, '13.3f'), 'Gallons'
    print "Consumption:", format(d, '10.3f'), 'L/100km', format(the_fuel_consumption_convert, '10.3f'), 'mpg'
    print "gas consumption rating:", fuel_rating





