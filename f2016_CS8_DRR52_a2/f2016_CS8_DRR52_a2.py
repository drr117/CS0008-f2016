def printKV (key, value, klen = 0): #setup a function that prints the output
    kl = max(len(key), klen) #variable that returns the largest value of the length of key, and klen
    if isinstance (value, str): #if the value is a string in all instances
        fs ='10s' #formatting
    elif isinstance (value, float):
        fs = '10.3f'
    if isinstance (value, int):
        fs = '-5'
    print(format(key, str(kl) + 's'),
            format (value, fs))


def processfile(x): #function to read and count the file
    num_line = 0 #initialize the variable for line numbers
    distance_x = 0 #initialize the variable for distance run
    for line in x: #for statement to count
        num_line = num_line+1
        contents = (x.readline()) #variable to read the lines on the text file
        contents.rstrip("\n")
        name, distance = contents.split (',') #splits the values between the comma
        if isinstance (distance, str): # converts the string values of distance
            distance = float(distance) #to float numbers
        distance_x = distance_x + distance #sets up a variable to add the distance
    printKV("Partial Distance Run:", distance_x) #prints the output according to the format of print kv
    printKV("Partial Number of Lines:", num_line) #does the same for the number of lines
    return(distance_x, num_line) #returns the two values

looper = 0 #create a value for the while loop
distance_x = 0 #set a value for the distance initially, this is for a running total

end_distance = 0 #these values are for the end of the program, when the user enters "quit"
end_n = 0
while looper == 0: #set
    x = str(input("Enter the name of the file you wish to open, or enter 'Quit' to end the program "))
    print ("\n")
    print ("File to be read:", x)
    if (x == 'q' or x == 'quit' or x=='Quit' or x == "'Quit'"):
        looper = 1
        printKV("Total Distance Run:", end_distance)
        printKV("Total Lines:", format(end_n, '15'))
    else:
        f = open(x, 'r')
        y_distance, y_n = processfile(f)
        end_distance = y_distance + end_distance
        end_n = y_n + end_n
