#PyPoll Homework

# Import as os and csv file
import os
import csv

# create path for csv file
pollcsv = os.path.join('Resources', 'election_data')

# create list for data
count = 0
candidatelist = []
vote_count = []
vote_percent = []

# open the csv file to set path
with open(pollcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #count the number of rows
    for row in csv_reader:
        count = count + 1
        #Candidate list
        candidatelist.append(row[2])