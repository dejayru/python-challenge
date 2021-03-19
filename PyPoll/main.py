#PyPoll Homework

# Import as os and csv file
import os
import csv

# create path for csv file
pollcsv = os.path.join('Resources', 'election_data')

# create list for data
total_vote_count = 0
candidates = []
vote_count = []
vote_percent = []

# open the csv file to set path
with open(pollcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #count the number of votes
    for row in csv_reader:
        total_vote_count = total_vote_count + 1
        #Candidate list
        candidates = row[2]

        if(candidates in candidates):
            candidates_index = candidates.index(candidates)
            vote_count[candidates_index] = vote_count[candidates_index] + 1

        else:
            candidates.append(row[2])
            total_vote_count.append(0)

    

        
