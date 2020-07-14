#import modules and csv file
import os
import csv

#counter used for counting candidates names
from collections import Counter

#file path for csv
budget_data = os.path.join( 'Resources', 'budget_data.csv')
      
#open and read csv file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #need to skip the header 
    csvheader = next(csvreader)

    #create variable holds total number of months of budget data and set to zero
    month_count = 0
    #create variable for total profit and losses an set to zero
    total_profit_losses = 0
    
    #loop through data
    for row in csvreader:

        #count to find number of months 
        month_count = month_count +1

        #use float variable to calculate total profit and losses
        float_profit_losses = float(row[1])
        total_profit_losses += float_profit_losses
        


#print header   
print("Financial Analysis")

#print formatting
print("-----------------------------")

#print total number of months
print(f"Total Months: {month_count}")

#print total of profit and loss
print(f"Total: {total_profit_losses}   ")
#print(f"Average Change:")
#print(f"Greatest Increase in Profits:")
#print(f"Greatest Decrease in Profits:")

#output_pybank = os.path.join('analysis', "main.txt")
#with open(output_pybank, "w") as txt.file:
