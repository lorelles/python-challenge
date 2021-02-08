import os
import csv
from statistics import mean

# Path to collect data from the resources folder
financial_csv = os.path.join("resources", "budget_data.csv")

# Assign lists to store data
total_months = []
net_amount = []
total_change = []
change_list = []
#max_increase = []
#max_decrease = []

# Read in CSV file
with open(financial_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)    
    #print(f"Header: {csv_header}")    
    
    #count = 0
    
    # Loop through data
    for row in csv_reader:
        ##date = string(financial_data[0])
        ##profit_losses = int(financial_csv[1])

        ## Assign values to variables with descriptive data
        
        # Add months
        total_months.append(row[0])   
        
        # Add amount
        net_amount.append(int(row[1]))
        
        # Calculate change in profit/loss
        total_change.append(row)

    #Calculate the monthly change in profit/loss
    ##Formula to calculate this value was obtained from Charlie Loveall who received the formula from his tutor.
    for idx, value in enumerate(total_change):
        if idx == 85:
            break
        change= int(total_change[idx+1][1])-int(total_change[idx][1])
        change_list.append(change)

#Determine total amount of months listed in data
total_mons = len(total_months) 

# Calculate net total amount of "Profit/Losses" over entire period
total_amount = sum(net_amount)

#Calculate average change in profit/losses over entire period
average_change = round(mean(change_list),2)

# Define function to calculate greatest increase in profits (Date and amount) over entire period
max_increase = round(max(change_list),2)

#print(total_change)
# Define function to calculate greatest decrease in losses (Date and amount) over entire period
max_decrease = round(min(change_list),2)

# Find total number of months in data set
#total_mons = len(total_months)
#print(total_mons)



## Script shoud print analysis to the terminal and export text file with results
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_mons}")
print(f"Total: ${total_amount}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits: ${max_increase}")
print(f"Greatest Decrease in Profits: ${max_decrease}")

output_file = os.path.join("PyBank.txt")