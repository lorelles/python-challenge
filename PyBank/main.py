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
max_increase = []
max_decrease = []
#mo_inc = []
#mo_dec = []

# Read in CSV file
with open(financial_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)    
    
    # Loop through data
    for row in csv_reader:

        ## Assign values to variables with descriptive data
      
        # Add months
        total_months.append(row[0])   
        
        # Add amount
        net_amount.append(int(row[1]))
        
        # Calculate change in profit/loss
        total_change.append(row)

        #Find months for max increase/decrease
        #if max_increase == 1926159
            

    #Calculate the monthly change in profit/loss
    ##Formula to calculate this value was obtained from Charlie Loveall who received the formula from his tutor.
    for idx, value in enumerate(total_change):
        if idx == 85:
            break
        change= int(total_change[idx+1][1])-int(total_change[idx][1])
        
        change_list.append(change)

    #for row in total_months:
        #if index == 24:
            #print(row)

    #for i in range(len(total_months)):
        #if list[i] == 24
            #return True
        #return False
        #print(i)

    #for row in total_months:
        #if row == -2196167:
            #print(row)
            #break

    #for row in total_months:
        #if row == 24:
            #mo_inc.append()
        #else:
            #break
            
        #elif i == -2196167:
            #mo_dec.append(row[0])
            #break

    #Find months for max increase/decrease   
    #if row == 1926159
        #print(row)

#Find the index of max/min then locate month with the index(account for header):

inc_index = change_list.index(1926159)
print(inc_index)
dec_index = change_list.index(-2196167)
print(dec_index)

mo_inc = total_months[24+1]
mo_dec = total_months[43+1]

#for idx, value in enumerate(total_months):
    #if idx ==24:
        #break
    #print(row)


#print(change_list)
#print(total_months)
#print(mo_inc)
#print(mo_dec)

#Determine total amount of months listed in data
total_mons = len(total_months) 

# Calculate net total amount of "Profit/Losses" over entire period
total_amount = sum(net_amount)

#Calculate average change in profit/losses over entire period
average_change = round(mean(change_list),2)

# Calculate greatest increase in profits (Date and amount) over entire period
max_increase = round(max(change_list),2)
#print(max_increase)


#Find months for max increase/decrease
#if max_increase == 1926159
    ##increse_mo 
#print(csv_reader.index(max_increase))

#Calculate greatest decrease in losses (Date and amount) over entire period
max_decrease = round(min(change_list),2)

#Find months for max increase/decrease
#with open(financial_csv, newline='') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")
    #csv_header = next(csv_file)    
    
    # Loop through data
    #for row in csv_reader:
        #if number == max_increase
        #print(row)
#print(max_row)

## Script shoud print analysis to the terminal and export text file with results
print("Financial Analysis")
print("-------------------")
#print(f"Total Months: {total_mons}")
print(f"Total: ${total_amount}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits: {mo_inc} $({max_increase})")
print(f"Greatest Decrease in Profits: {mo_dec} $({max_decrease})")

output_file = os.path.join("PyBank.txt")