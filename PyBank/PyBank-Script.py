#import os and csv modules
import os

import csv

#Set path for file
csvpath = os.path.join("GitHub", "Python_Challenge", "PyBank", "Resources", "budget_data.csv")

print("Financial Analysis")
print("---------------------------------")

#Open the CSV file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Set lists to store the required data for totals
    date = []
    profit_or_loss = []
    changes_per_month = []

    #Set required variables to zero
    dates = 0
    total_profit_or_loss = 0
    total_change_profitloss = 0
    beginning_profitloss = 0

    #Create for loop to determine total months and profit/losses
    for row in csvreader:
        
        #Dates are retrieved from first column of dataset
        date.append(row[0])

        #Profits/Losses are retrieved from second column of dataset
        profit_or_loss.append(int(row[1]))

    #Calculate total months
    dates = len(date)
    print("Total Months: " + str(dates))

    #Calculate total Profit/Losses
    total_profit_or_loss = sum(profit_or_loss)
    print("Total: " + str(total_profit_or_loss))

    #Create for loop to determine Average, Max and Min
    for x in range(1,len(profit_or_loss)):
        changes_per_month.append(profit_or_loss[x] - profit_or_loss[x -1])

    #Calculate Average, Max and Min
    average = sum(changes_per_month) / (dates - 1)
    print("Average: " + str(average))

    max = max(changes_per_month)
    max_date = date[changes_per_month.index(max) + 1]
    print(f"Greatest Increase in Profits: ", (max_date), (max))

    min = min(changes_per_month)
    min_date = date[changes_per_month.index(min) + 1]
    print(f"Greatest Decrease in Profit: ", (min_date), (min))

#Export a text file with the results.
txtpath = os.path.join("GitHub", "Python_Challenge", "PyBank", "analysis", "results.txt")

with open(txtpath, 'w') as text:
    text.write("Financial Analysis")
    text.write("-------------------------------")
    text.write("Total Months: " + str(dates))
    text.write("Total: " + str(total_profit_or_loss))
    text.write("Average: " + str(average))
    text.write("Greatest Increase in Profits: " + str(max_date) + str(max))
    text.write("Greatest Decrease in Profit: " + str(min_date) + str(min))









