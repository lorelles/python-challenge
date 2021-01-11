import os
import csv

# Path to collect data from resources folder
election_csv = os.path.join("PyPoll/resources", "election_data.csv")

# Lists to store data
votes = []
candidates = []
percent_won = []
total_won = []
winner = []


# Read in the CSV file
with open(election_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    # Loop through the data
    for row in csv_reader:

        # Define function to calculate total number of votes cast
        votes.append(row[0])
        votes = len(votes)

        # Define function to create list of candidates who received votes
        candidates.append(row[3])
        ##candidates = 

        # Define function to calculate percentage of votes each candidate won
        percent_won.append(row[3])
        ##percent_won = round(int(row[]) / int(row[]), 2)

        # Define function to calculate total number of votes each candidate won
        total_won.append(row[3])
        ##total_won =

        # Define function to calculate winner of election based on popular vote
        winner.append(row[3])
        ##winner = 

# Final script should both print the analysis to the terminal and export a text file with the results
##output_file = os.path.join("PyPoll.txt")
