overall_file = input("Enter the location of your file") #lets the user select the location of the file
global_dict = {} #creates a dictionary outside the function
def processfile (overall_file, global_dict): #function for the two previous values and allows for the processing of one file that contains multiple files
    contents_overall_file = open(overall_file, 'r') #opens the file that contains the names of the other files
    files = contents_overall_file.readlines() #reads the overall file and reads the names within the file
    for line in contents_overall_file: #for loop that iterates over the values inside the overall file
        file_name = line.rstrip('\n') #removes the newline character from each value
        length_oaf = len(files) #takes the length of the files
        print (file_name) #prints the names of the files to be opened
        x = open (file_name, 'r') #opens the files in the overall file and allows for them to be read
        x.readline() #this initial readline skips over the "name" and "distance" so they aren't used in the file
        for line in x: #another for loop to read the lines in the individual file
            print (line) #why is this here?
            line = line.rstrip('\n') #eliminates the newline character from the values in each file
            name, dist = line.split(',') #splits the values between the commas and names them "name" and "dist" respectively
            p_dist = int(dist) #makes an integer value for distance and sets it equal to distance
            t_dist = 0 #initializes the accumulator value
            t_dist += p_dist #running total for the partial distance
            if name in dict: #if statement for the dictionary in the event that a name appears twice
                dict{name} = dict{}.append{line,list}






