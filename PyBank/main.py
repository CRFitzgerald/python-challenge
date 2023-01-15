# import os module to create file paths across operating systems
import os

#import module for reading CSV files
import csv

# read using CSV module
csvpath = os.path.join ("Resources" , "budget_data.csv")
with open(csvpath, encoding='utf') as budgetfile:

    # specify variable holding contents & delimiter
    csvreader = csv.reader(budgetfile, delimiter=',')
    
    # set initial row_count value to 1
    row_count = 1
    
    # skip header
    header = next(csvreader)
    
    # create variable for first row
    first_row = next(csvreader)
    
    # set variable for Total Profits and Losses
    total = int(first_row[1])
    
    # set variable for previous row (useful for finding monthly revenue change)
    prev_net = int(first_row[1])
    
    # variable to hold list of monthly changes in revenue. will use for average change
    list_rev_change = []
    
    # set initial lowest value very high to guarantee all actual data will be lower
    lowest_val = 100000000
    
    # set initial highest value very low to guarantee all actual data will be higher
    highest_val = -1000000000
    
    # variable to contain lowest value month
    lowest_val_month = ""
    
    #variable to contain highest value month
    highest_val_month = ""
        
    # read each row after header
    for row in csvreader:
        
        # count number of months
        row_count+= 1
        
        # sum total profits and losses
        total = total + int(row[1])
        
        # calculate change between each row, ie row3 - row2 = rev_change
        rev_change = int(row[1]) - prev_net
        
        #calculate Greatest Increase in Profits
        if rev_change > highest_val:
            highest_val = rev_change
            highest_val_month = row[0]
        
        #calculate Greatest Decrease in Profits
        if rev_change < lowest_val:
            lowest_val = rev_change
            lowest_val_month = row[0]
        prev_net = int(row[1])

        # populate list of all changes in revenue
        list_rev_change = list_rev_change + [rev_change]

        # calculate average of revenue change values found in list
        avg_rev_change = round(sum(list_rev_change)/len(list_rev_change),2)

# print line show analysis is starting
print('-' * 25)

# print title
print ("Financial Analysis")

# print line to separate title from data
print('-' * 25)

# print number of months
print (f"Total Months: {row_count}")
        
# print total profits and losses
print (f"Total: ${total}")

# print Average Change
print (f"Average Change: ${avg_rev_change}")

# print Greatest Increase amount
print (f"Greatest Increase in Profits: {highest_val_month} ${highest_val}")

# print Greatest Decrease amount
print (f"Greatest Decrease in Profits: {lowest_val_month} ${lowest_val}")

# Export above results to .txt file in addition to terminal
# Specify .txt file to write to
output_path = os.path.join("Analysis", "PyBank-Analysis.txt")

# Open the file using "write" mode. Specify variable to hold contents
with open(output_path, 'w') as bank_analysis:
    results = (f"------------------------\n"
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Months: {row_count}\n"
    f"Total: ${total}\n"
    f"Average Change: ${avg_rev_change}\n"
    f"Greatest Increase in Profits: {highest_val_month} ${highest_val}\n"
    f"Greatest Decrease in Profits: {lowest_val_month} ${lowest_val}")
        
    bank_analysis.write(results)
