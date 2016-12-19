# name       : Darius Ramavarapu
# email      : DRR52@pitt.edu
# date       : 2016/12/15
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Final Project
#
# Description:
# A customer needs to process a number of text files (called data files) that contain names and distance run by study participants.
# The format of those files is as follows:
#
# Max ,34.23
# Barbara ,23.00
# Luka ,12.87
# …
#
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant and the
# second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
#
# <data file 1>
# <data file 2>
# <data file 3>
# …
#
# Write a program that read the master input list file, retrieves the names of the data files and from each one of them
# reads every line, extract name and distance. Once the program has all the data in memory, it has to compute the following
# quantities and informations:
# - number of files read in input
# - total number of lines read
# - total distance run (aka the sum of all the distances loaded from provided files)
# - total distance run for each individual participant
# - individual maximum distance run and by which participant
# - individual minimum distance run and by which participant
# - report if there are any participants that appears more than once, how many times and their names
# - total number of participants
#
# The program should provide an terminal output similar to the following:
#
#	Number of Input files read   : xx
#	Total number of lines read   : xx
#
#	total distance run           : xxxx.xxxxx
#
#	max distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	min distance run             : xxxx.xxxxx
#	  by participant             : participant name
#
#	Total number of participants : xx
#	Number of participants
#    with multiple records       : xx
#
# The program should also create an output file reporting name of the participant, how many times their name appears in
# the input files and the total distance run. Each row should be as follows:
#
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87
# …
#
# In this program, the student should make the best use of everything that has learn so far in this class,
# reuse as much as he/she can from assignment #3, improve upon it and he/she has to use a class named participants
# that has 3 properties:
# - name: name of the participant. String.
# - distance: accumulator for total distance run by the participant. Float.
# - runs: accumulator for the total number of runs run by the participant.
#
# and, at least, the following methods:
# - addDistance(d)
#   add single distance to the distance accumulator and increments runs by 1. Argument d is a single float.
# - addDistances(ld)
#   add an array of distances to distance accumulator. Argument ld is a list of floats. getDistance()
#   get the current value of the distance accumulator.
# - getName()
#   get the name of the participant of the current instance
# - getDistance()
#   get the total distance run computed
# - getRuns()
#   get the total number of runs
# - __init__ (n,d=0)
#   initializer method. set name and initial distance if provided. If initial distance is not specified,
#   it should be set to zero
# - __str__()
#   stringify method. Returns a string with name, total distance run and how many distances the object added,
#   according to the following format:
#   Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
#
#   where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name,
#   yyyy.yyyy is the total distance run with 9 digits, decimal point and 4 decimals,
#   and zzzz is the number of runs with 4 digits, no decimals.
#

#
# class participant definition according to specs from header
# class definition


#establish a class
class participant:
    #initialize variables
    n = "unknown"
    run = 0
    #set up method (private)
    def __init__(self,n, d =0):
        #attributes
        self.name = n
        self.distance = d
        #if statement
        if d == 0:
            #run isn't counted if d==0
            self.run = 0
            #any other value run is counted
        else:
            self.run = 1
    #public method
    def addDistance(self,d):
        #if d > 0 then accumulate distance and run
        if d > 0:
            self.distance += d
            self.run += 1
    #public method
    def addDistances(self, distances):
        #loops over list distances and performs addDistance
        for distance in distances:
            self.addDistance(distance)
    #public method
    def getDistance(self):
        #returns distance
        return self.distance
    #public method
    def getrun(self):
        #returns runs by participant
        return self.run
    #public method
    def getName(self):
        #returns name of participant
        return self.name
    #stringify method (private)
    def __str__(self):
        #formats the public methods name, distance, and runs
        return \
            "Name : " + format(self.name, '>20s') + \
            ". Distance run : " + format(self.distance, '9.4f') + \
            ". Runs : " + format(self.run, '4d')


    #public method
    def tocsv(self):
        #returns name runs and distance with a comma between them
        return ','.join([self.name, str(self.run), str(self.distance)])
#end class

def accessdata(file):
    # output is initialized in a list
    output = []
    # loop to read lines
    for line in open(file,'r'):
        #skip over distance
        if "distance" in line:
            #if distance is presesnt, it is skipped over
            continue
        # remove \n ending the line and split line at ","
        temp1 = line.rstrip('\n').split(',')
        # eliminates improperly formatted lines
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})
        except:
            print('Invalid row : '+line.rstrip('\n'))
        # end try/except

    return output
#def is complete
#
# ask for master file from user
masterFile = input("Please provide the master file : ")

# read master file and extract data files
try:
    dataFiles = [file.rstrip('\n') for file in open(masterFile,'r')]
except:
    print("Impossible to read master file or invalid file name")
    exit(1)
# end try/except

# read data from data files
# we assume that the data files are accessible locally or we have the full path
#
# rawData is a list of all the records from each data file
#for some reason the other form of this (as a separate empty list, and then a for loop caused an error by providing too much data)
rawData = sum([accessdata(file) for file in dataFiles],[])
#
numberFiles = len(dataFiles)

#
# total number of lines read
# this is equivalent to the sum of the second item in each item of rawData
totalLines = len(rawData)
totalDistanceRun = sum([item['distance'] for item in rawData])

#
# compute distance run for each participant and how many records present each one of them
# initialize  accumulators
# empty dictionary for the participants and their distances
participants = {}

# loop on all the records
for item in rawData:
    # check if the names has already been found previously or if it is new
    # if it is new, initialize elements in the accumulators
    if not item['name'] in participants.keys():
        participants[item['name']] = participant(item['name'])
    # insert distance in the list for this participant
    participants[item['name']].addDistance(item['distance'])
# end for

# initialize accumulators
# minum distance run with name
minDistance = { 'name' : None, 'distance': None }
# maximum distance run with name
maxDistance = { 'name' : None, 'distance': None }
# appearences dictionary
apparences = {}
#
# computes the total distance run for each participant iterating on all the participants
for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistance()
    # check if we need to update min
    # if this is the first iteration or if the current participant distance is lower than the current min
    if minDistance['name'] is None or minDistance['distance'] > distance:
        minDistance['name'] = name
        minDistance['distance'] = distance
    # end if
    # check if we need to update max
    # if this is the first iteration or if the current participant distance is lower than the current min
    if maxDistance['name'] is None or maxDistance['distance'] < distance:
        maxDistance['name'] = name
        maxDistance['distance'] = distance
    # end if
    #
    # get number of runs, aka apparences from participant object
    participantAppearences = object.getrun()
    #
    # check if we need to initialize this entry
    if not participantAppearences in apparences.keys():
        apparences[participantAppearences] = []
    apparences[participantAppearences].append(name)
# end for

#
# compute total number of participant
# this is equivalent to the length of the participantDistances
totalNumberOfParticipant = len(participants);

#
# compute total number of participants with more than one record
# extract all the participants that have 2 or more runs
# and count th enumber of elements in the list with len()
totalNumberOfParticipantWithMultipleRecords = len([1 for item in participants.values() if item.getrun() > 1])

#
# set format strings
INTEGER = '5d'
FLOAT = '12.5f'
STRING = '20s'

#
# provide requested output
print("")
print(" Number of Input files read   : " + format(numberFiles,INTEGER))
print(" Total number of lines read   : " + format(totalLines,INTEGER))
print("")
print(" Total distance run           : " + format(totalDistanceRun,FLOAT))
print("")
print(" Max distance run             : " + format(maxDistance['distance'],FLOAT))
print("   by participant             : " + format(maxDistance['name'],STRING))
print("")
print(" Min distance run             : " + format(minDistance['distance'],FLOAT))
print("   by participant             : " + format(minDistance['name'],STRING))
print("")
print(" Total number of participants : " + format(totalNumberOfParticipant,INTEGER))
print(" Number of participants")
print("  with multiple records       : " + format(totalNumberOfParticipantWithMultipleRecords,FLOAT))
print("")

#
# create output file
outputFile = "f2016_cs8_DRR52_a3.output.csv"
# open file for writing
fh = open(outputFile,'w')
# write header in file
fh.write('name,records,distance\n')
# loop on all the participants
for name, object in participants.items():
    # write line in file
    fh.write(object.tocsv() + '\n')
#end for
# close files
fh.close()






