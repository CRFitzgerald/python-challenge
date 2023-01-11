# import module to create path through multiple systems
import os

# import module to read CSV files
import csv

# read PyPoll CSV file
csvpath = os.path.join ("Resources" , "election_data.csv")
with open(csvpath, encoding='utf') as pollfile:

    # specify var holding contents and delimiter
    csvreader = csv.reader(pollfile, delimiter=',')
    
    # skip header
    header = next(pollfile)
    
    # create variable for first row
    first_row = next(pollfile)
    
    # create list of candidates and assign variable to it
    candidates = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
    
    # set initial row_counter value to 1 to for correct starting point
    row_count = 1
    
    # create variable to contain votes for Stockham and set to 1 bc header
    stockham_votes = 1
    
    # create variable to contain votes for DeGette
    degette_votes = 0
    
    # create variable to contain votes for Doane
    doane_votes = 0
    
    # create empty variable to contain name of winner
    winner = ""
    
    # read each row
    for row in csvreader:
    
        # count number of votes
        row_count+= 1
        
        # count each candidate's votes
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes += 1
            
#create variable to contain Stockham's vote percentage
stockham_percentage = round(stockham_votes/row_count*100,3)

#create variable to contain DeGette's vote percentage
degette_percentage = round(degette_votes/row_count*100,3)

#create variable to contain Doane's vote percentage
doane_percentage = round(doane_votes/row_count*100,3)

#create list to contain each candidate's vote counts
votes_counts = [stockham_votes , degette_votes , doane_votes]

# create variable to contain most votes and set to low number to capture all results
most_votes = -10000

# create generic variable for candidates respective votes to make them easy to compare to each other and set that variable to 0
candidate_votes = 0

# zip together list of candidate names and their respective votes
votes_per_candidate = zip(candidates, votes_counts)

# for-loop through zipped list
for candidates in votes_per_candidate:
    
    # set candidates_votes variable's position
    candidate_votes = candidates[1]
    
    #conditional to find candidate w/ most votes ie winner
    if candidate_votes > most_votes:
        most_votes = candidate_votes
        winner = candidates[0]

# print line to show results are starting
print ("-" * 25)
# print title
print ("Election Results")
# print line to separate title from data
print ("-" * 25)
# print total votes
print ("Total Votes:", row_count)
# print each candidate's name, percentage of total vote won, and vote count
print (f"Charles Casper Stockham: {stockham_percentage}% ({stockham_votes})")
print (f"Diana DeGette: {degette_percentage}% ({degette_votes})")
print (f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})")
# print lime to separate winner from data
print ("-" * 25)
# print winner
print (f"Winner: {winner}")
# print line for ending
print ("-" * 25)

# Export above results to .txt file in addition to terminal
# Specify .txt file to write to
output_path = os.path.join("Analysis", "PyPoll-Analysis.txt") #class 3.2 slide 42

# Open the file using "write" mode. Specify variable to hold contents
with open(output_path, 'w') as poll_analysis:
    results = (f"------------------------\n"
    f"Election Results\n"
    f"------------------------\n"
    f"Total Votes: {row_count}\n"
    f"Charles Casper Stockham: {stockham_percentage}% ({stockham_votes})\n"
    f"Diana DeGette: {degette_percentage}% ({degette_votes})\n"
    f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})\n"
    f"------------------------\n"
    f"Winner: {winner}\n"
    f"------------------------\n")
    
    poll_analysis.write(results)
