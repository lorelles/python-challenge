import os
import csv
from statistics import mean

# Path to collect data from the resources folder
financial_csv = os.path.join("resources", "budget_data.csv")

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
        # Add months
        total_months.append(row[0])    
        # Add amount
        net_amount.append(int(row[1]))
        ###net_amount.append(int(row[1]-row[0]))
        # Add change in profit/loss
        ##total_change.append(row)
        # Add greatest increase change
        #max_change.append(int(row[1]))
        # Add greatest decrease in change
        #max_decrease.append(int(row[1]

        # Define function to calculate changes in "Profit/Losses" over entie period
        #total_change = sum(total_change)

        # Then find average of changes in "Profit/Losses"
        ##mean_change = total_change.mean

        # Define function to calculate greatest increase in profits (Date and amount) over entire period
        ##max_increase = net_amount.max


# Define function to calculate greatest decrease in losses (Date and amount) over entire period
# #max_decrease = net_amount.min

# Define function to calculate greatest increase in profits (Date and amount) over entire period
##max_increase = net_amount.max

# Find total number of months in data set
total_mons = len(total_months)
#print(total_mons)

 # Calculate net total amount of "Profit/Losses" over entire period
total_amount = sum(net_amount)
#print(f"The total amount of Profit/Loss is:")
#print(total_amount)



## Script shoud print analysis to the terminal and export text file with results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_mons}")
print(f"Total Profit/Losses : ${total_amount}")
#print(f"Average Change:  #{}")
#print(f"Greatest Increase in Profits: ${}")
#print(f"Greatest Decrease in Profits: ${}")

output_file = os.path.join("PyBank.txt")