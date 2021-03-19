#PyBank Homework

# Import as os and csv file
import os
import csv

# create path for csv file
bankcsv = os.path.join('..', 'Resources', 'budget_data.csv')


# create list for data
profit = []
month_changes = []
date = []

# set variables
count = 0
total_profit = 0
total_change_profits = 0
inital_profit = 0

# open the csv file to set path
with open(bankcsv, 'r') as csvfile:
    csv_reader = next(csv_reader, delimiter=',')
    csv_headers = next(csv_reader)

    #count the number of months in data file
    for row in csv_reader:
        count = count + 1
    #append the date
        date.append(row[0])
    # profit infomation to calc total profit

    #calc avg change in profits month to month

    #create list of monthly changes

    #calc the avg change month to month

    #get max/min for change in profits and dates

#analysis output

#output as text

