a = input("SELECT USC OR METRIC AS YOUR UNIT CHOICE; (SELECT 'METRIC' or 'USC')") #Create an input statement to let the user select what they want
b = float(input("How far did you travel?")) #create an input statement for distance
c = float(input("How Much gas did you use?")) #do the same for gas usage
d = b/c #calculate fuel usage
if (a == "USC"):
    print (b, "miles")
    print (c, "gallons")
    print (d, "mpg")
    e = d * (62.1371/26.4172)
    print (e)
    if (e > 20):
        print("Extremely Poor")
    elif (e > 15 and e <= 20):
        print("Poor")
    elif (e > 10 and e <= 15):
        print ("Average")
    elif (e > 8 and e <= 10):
        print ("Good")
    elif (e <= 8):
        print ("Excellent")
else:
    if (a == "METRIC"):
        print (b, "Kilometers")
        print (c, "Liters")
        f = d *(1/100)
        print (d, "Liters/100km")
        e = f
        print (e)
        if (e > 20):
            print("Extremely Poor")
        elif (e > 15 and e <= 20):
            print("Poor")
        elif (e > 10 and e <= 15):
            print ("Average")
        elif (e > 8 and e <= 10):
            print ("Good")
        elif (e <= 8):
            print ("Excellent")






