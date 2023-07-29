#import os and csv modules
import os

import csv

#Set path for file
csvpath = os.path.join("GitHub", "Python_Challenge", "PyPoll", "Resources", "election_data.csv")

print("Election Results")
print("-------------------------------------")

#Open the CSV file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Set lists to store required data for totals
    list_of_candidates = []
    candidate_name = []
    total_votes = []
    percentage_votes = []

    #Set required variables to zero
    voter_count = 0

    #Create for loop to determine total votes
    for row in csvreader:

        #Total votes are retrieved from first column of dataset
        total_votes.append(row[0])

        #Set names of candidates to list
        list_of_candidates.append(row[2])

    #Calculate voter counts
    voter_count = len(total_votes)
    print("Total Votes: " + str(voter_count))
    print("--------------------------------------------")

    #Create a for loop to retrieve candidate names and results
    for name in set(list_of_candidates):
        candidate_name.append(name)
        
        #Retrieve total number of votes per candidate
        votes_per_candidate = list_of_candidates.count(name)
        total_votes.append(votes_per_candidate)

        #Retrieve total percentage of votes per candidate
        total_percent_candidate = (votes_per_candidate/voter_count)*100
        percentage_votes.append(total_percent_candidate)

    #Create a loop to list each candidate results
    for x in range(len(candidate_name)):
        print(candidate_name[x] + ": " + str(percentage_votes[x]) + "% " + str(total_votes[x]))

    print("----------------------------------")

#Export a text file with the results
txtpath = os.path.join("GitHub", "Python_Challenge", "PyPoll", "analysis", "results.txt")

with open(txtpath, 'w') as text:
    text.write("Election Results")
    text.write("-------------------------------")
    text.write("Total Votes: " + str(voter_count))
    for x in range(len(candidate_name)):
        text.write(candidate_name[x] + ": " + str(percentage_votes[x]) + "% " + str(total_votes[x]))
    text.write("------------------------------------------")






