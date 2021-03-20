#PyPoll Homework

# Import as os and csv file
import os
import csv

# create path for csv file
pollcsv = os.path.join('Resources', 'election_data.csv')

# create list for data
candidates = []
candidates_votes = {}
vote_count = 0
winner_votes = 0
percentages = []
max_votes = 0
max_index = 0


# open the csv file to set path
with open(pollcsv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)

    #count the number of votes
    for row in csv_reader:
        vote_count = vote_count + 1
        candidates_name = row[2]
        #Candidate list
        if (row[2]) not in candidates:
            candidates.append(row[2])
            candidates_votes[candidates_name] = 0
         
        candidates_votes[candidates_name] = candidates_votes[candidates_name] + 1
        
        

    #print(vote_count)    
    #print(candidates_votes)
    #print(candidates)                         
    #Percentage of votes and winner
    for count in candidates_votes:
        percentages = candidates_votes[count] / vote_count * 100
        #print(count)
        
        if candidates_votes[count] > winner_votes:
            winner = count
            winner_votes = candidates_votes[count]

    

#Results
    print('.........................................')
    print("Election Results")
    print('.........................................')
    print("Total Votes: " + str(vote_count))
    print('.........................................')
    for count in candidates_votes:
        percentages = candidates_votes[count] / vote_count * 100
        print(f"{count}: {percentages}% ({candidates_votes[count]})")
    print('.........................................')
    print(f"The Winner is:  {winner}")
    print('.........................................')

# Text File
with open ('Election Results.txt', 'w') as text:
    text.write(".............................................\n")
    text.write("    Election Results"+ "\n")
    text.write("...............................................\n\n")
    text.write("    Total Votes: " + str(vote_count) + "\n")
    text.write("...............................................\n\n")
    for count in candidates_votes:
        percentages = candidates_votes[count] / vote_count * 100
        text.write(f"{count}: {percentages}% ({candidates_votes[count]})")
    text.write("...............................................\n\n")
    text.write("    The Winner is {winner}\n")
    text.write("...............................................\n\n")