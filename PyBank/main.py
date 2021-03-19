#PyBank Homework

# Import as os and csv file
import os
import csv

# create path for csv file
bankcsv = os.path.join('Resources', 'budget_data.csv')


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
with open(bankcsv, newline='') as csvfile:
    csv_reader = csv.reader(csv_reader, delimiter=',')
    csv_headers = next(csv_reader)

    #count the number of months in data file
    for row in csv_reader:
        count = count + 1
    #append the date
        date.append(row[0])
    # profit infomation to calc total profit
        profit.append(row[1])
        total_profit = total_profit + int(row[1])

    #calc avg change in profits month to month
        final_profit = int(row[1])
        month_changes_profits = final_profit -  inital_profit
    #create list of monthly changes
        month_changes.append(month_changes_profits)

        total_change_profits = total_change_profits + month_changes_profits
        inital_profit = final_profit
    #calc the avg change month to month
        average_change_profits = (total_change_profits/count)

    #get max/min for change in profits and dates
        largest_increase_profits = max(month_changes)
        largest_decrease_profits = min(month_changes)

        Increase_date = date[month_changes.index(largest_increase_profits)]
        decrease_date = date[month_changes.index(largest_decrease_profits)]

#analysis output
    print('.........................................')
    print("Financial Analysis")
    print('.........................................')
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change " + "$" +str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(Increase_date) + " ($" + str(largest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(largest_decrease_profits) + ")")
    print('.........................................')

#output as text
with open('Financial_analysis.txt', 'w') as text:
    text.write(".............................................\n")
    text.write("   Financial Analysis"+ "\n")
    text.write("...............................................\n\n")
    text.write("      Total Months: " + str(count) + "\n")    
    text.write("      Total Profits: " + "$" + str(total_profit) + "\n")
    text.write("      Average Change: " + "$" + str(int(average_change_profits)) + "\n")
    text.write("      Greatest Increase in Profits: " + str(Increase_date) + " ($" + str(largest_increase_profits) + ")\n")
    text.write("      Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(largest_decrease_profits) + ")\n")
    text.write(".............................................\n")