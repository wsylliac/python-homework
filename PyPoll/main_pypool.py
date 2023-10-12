from operator import index
import os

import csv
#The collection of the data from the resources folder 
csvpath = os.path.join('Resources_pypool', 'election_data.csv') 
output = '''Election Results
-------------------------
Total Votes:'''
''' 369711
-------------------------
Charles Casper Stockham: 23.049% 85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
'''

with open (csvpath, encoding='utf') as csvfile:
    #Read the csvfile 
    csvreader = csv.reader(csvfile, delimiter=',')

#skip the first row (header)
next(csvreader)

total_votes = []
candidates_votes = ()

#Total number of the votes 

for line in csvreader:
        total_votes.append(line[2])
total_count = len (total_votes)
output = output + str(total_count) + "\n-------------------------" + "\n"
candidates= list(set(total_votes))
votes_per_candidate = []
percentage = []

#The votes per candidate
#List of the canddiates 
for candidate in candidates:
    votes_per_candidate.append(total_votes.count(candidate))

#The percentage of votes for each candidate 
for i in range (len(candidates)):
    percentage = votes_per_candidate[i]/total_count*100
    output = output + f'{candidates[i]}: {round(percentage, 3)}% ({votes_per_candidate[i]}) \n'
#Winner of the vote
index_of_winner = votes_per_candidate.index(max(votes_per_candidate))
output = output + f"-------------------------\nWinner: {candidates[index_of_winner]}\n-------------------------"


#The results are being exported to text file and print on the terminal
print(output)
csvpath = os.path.join('Analysis', 'Polling_Analysis.txt')
with open(csvpath, 'w') as textfile:
    textfile.write(output)