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
percentages = []
max_votes = vote_count[0]
max_index = 0

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

    #Percentage of votes and winner
    for count in range(len(candidates)):
        vote_percent = vote_count[count]/number_votes*100
        percentages.append(vote_percent)
        if vote_count[count] > max_votes:
            max_votes = vote_count[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]

    percentages = [round(i,2) for i in percentages]

#Results
    print('.........................................')
    print("Election Results")
    print('.........................................')
    print("Total Votes: " + str(count))
    print('.........................................')
    for count in range(len(candidates)):
        print(candidates[count] + ": " + str(percentages[count]) + "% (" + str(vote_count[count]) + ")")
    print('.........................................')
    print("The Winner is: + {winner}"
    print('.........................................')

# Text File
with open ('Election Results.txt', 'w') as text:
    text.write(".............................................\n")
    text.write("    Election Results"+ "\n")
    text.write("...............................................\n\n")
    text.write("    Total Votes: " + str(count) + "\n")
    text.write("...............................................\n\n")
    for count in range(len(candidates)):
        print(candidates[count] + ": " + str(percentages[count]) + "% (" + str(vote_count[count]) + ")" +"\n")
    text.write("...............................................\n\n")
    text.write("    The Winner is {winner}\n")
    text.write("...............................................\n\n")