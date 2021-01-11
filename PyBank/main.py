import os
import csv
from statistics import mean

# Path to collect data from the resources folder
financial_csv = os.path.join("PyBank/resources", "budget_data.csv")

# Assign lists to store data
total_months = []
net_amount = []
#total_change = []
#mean_change = []
#max_increase = []
#max_decrease = []

# Read in CSV file
with open(financial_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)    
    #print(f"Header: {csv_header}")    
    
    # Loop through data
    for row in csv_reader:
        ##date = string(financial_data[0])
        ##profit_losses = int(financial_csv[1])

        # Assign values to variables with descriptive data
        total_months.append(row[0])    

        net_amount.append(int(row[1]))

        #total_change.append(row)

        #max_change.append(int(row[1]))

        #max_decrease.append(int(row[1]

        # Define function to return number of months included in dataset
        mons = len(total_months)

        # Define function to calculate net total amount of "Profit/Losses" over entire period
        total_amount = sum(net_amount)
        print(total_amount)

        # Define function to calculate changes in "Profit/Losses" over entie period
        #total_change = sum(total_change)

        # Then find average of changes in "Profit/Losses"
        ##mean_change = total_change.mean

        # Define function to calculate greatest increase in profits (Date and amount) over entire period
        ##max_increase = 

        # Define function to calculate greatest decrease in losses (Date and amount) over entire period
        #max_decrease =

## Script shoud print analysis to the terminal and export text file with results
#output_file = os.path.join("PyBank.txt")