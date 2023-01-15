# python-challenge
UCB Virtual Data Analytics Module 3 Challenge

Overview: Python code is used to find and calculate data points from two .csv files:

PyPoll:

  Resources folder contains csv list of individual ballots with their district and preferred candidate. All data points in PyPoll are based on this file. Any change or defect of this file would corrupt all data and analysis found in PyPoll folder.
  
  main.py is where all code is located. Code is 100% python. Using for loops, it counts votes as well as how many ballots contain each candidate's name. Candidate name list created and votes per           candidate list are created and zipped together. For loops through the zipped list determine winner.     Election Results are printed both in Terminal as well as creating a .txt file found in Analysis         folder.
  
  Analysis folder contains election results txt file. Contents of this file should be the same as what is printed in terminal.
  
PyBank:
  
  Resources folder contains csv list of fiscal months with respective revenue gained or lost. All     data points in PyBank are based on this file. Any change or defect of this file would corrupt all data and analysis found in PyBank folder.
    
  main.py is where all code is located. Code is 100% python. Using for loops, it tracks month-to-month changes in revenue and performs calculations to find total months being tracked, sum of all       revenue during this period, average monthly change in revenue, as well as greatest month-to-month       increase and decrease. Financial Analysis are printed both in Terminal as well as creating a .txt       file found in Analysis folder.
    
  Analysis folder contains election results txt file. Contents of this file should be the same as    what is printed in terminal.
    
Results: After running main.py code found in PyPoll and PyBank folders, the below was              determined.
    
PyPoll: 
    
  There was a total of 369,711 votes cast.
  Charles Casper Stockham won 23.049% of those votes with 85213 cast for him.
  Diana DeGette won 73.812% of those votes with 272,892 cast for her.
  Raymon Anthony Doane won 3.139% of those votes with 11,606 case for him.
  Diana DeGett won the election.
    
    
PyBank:
    
  Eighty-six consecutive months were tracked, beginning January 2010.
  The sum of all revenue during this time was $22,564,198.
  Average change month to month was a loss of $8311.11.
  Greatest month to month increase in revenue occured August 2016. It was an increase of                 $1,862,002.
  Greatest month to month loss of revenue occured February 2014. It was a loss of $1,825,558.
  
Analysis:

PyPoll: Diana DeGette has a clear mandate to govern. Stockham and Doane's combined votes are 35% of DeGette's total. Was DeGette's runaway victory the result of personal charisma, name recognition, greater spending or smarter spending? 

It would be interesting to see total campagin spending per candidate, what buckets it was spent in (printed mail ads vs. TV ads vs. costs associated with in person events, for example), as well as the number of donations compared to size of donation in a scatter plot. Other possible factors include years in office, candidate age, and voter age. 

PyBank: Is this a money laundering operation? Financial records are disturbingly lax with zero itemization of money in/money out. This business is ripe to be audited by the IRS.

With the average month-to-month change being a loss in the thousands of dollars, it is questionable how this business has continued to run for this many years as operating costs have only risen. Benefit of the doubt would say that the average change is being thrown off by an outlier decrease month, however the greatest increase and decrease months essentially cancel each other out (each in the low millions with an absolute difference of approximately $36k). 
    
    
    
