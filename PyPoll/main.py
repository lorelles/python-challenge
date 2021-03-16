import os
import csv

# Path to collect data from resources folder
election_csv = os.path.join("resources", "election_data.csv")

# Lists to store data
votes = []
names = []
#candidates = []
#all_candidates = []
#percent_won = []
#total_won = []
#winner = []

# Read in the CSV file
with open(election_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    # Loop through the data
    for row in csv_reader:

        # Define function to calculate total number of votes cast
        votes.append(row[0])
        total_votes = len(votes)

        # Define function to create list of candidates who received votes
        names.append(str(row[2]))

        # Use dictionary-add each candidate and vote count, if already exists acces candidate key, add vote count
        candidates = {}
        i = 0
        for name in names:
            if name[i] == name:
                candidates[name] += 1
            else:
                candidates[name] = 1
                break

#print(candidates)

#for name in names:
    #if name[i] == name:
        #candidates["name"] += 1
    #else:
        #candidates["name"] = 1
                #break
                
        # Define function to calculate percentage of votes each candidate won
        #percent_won.append(row[3])
        #percent_won = round(int(row[]) / int(row[]), 2)

        # Define function to calculate total number of votes each candidate won
        #total_won.append(row[3])
        ##total_won =

        # Define function to calculate winner of election based on popular vote
        #winner.append(row[3])
        ##winner = 
        ###Append Dict for values 

# Final script should both print the analysis to the terminal and export a text file with the results
print("Election Results")
print("---------------------")
print(f"Total Votes: {total_votes}")
print("---------------------")
##print("")
##print("")
##print("")
##print("")
print("---------------------")
print(f"Winner: {candidates}")
print("---------------------")

output_file = os.path.join("PyPoll.txt")
