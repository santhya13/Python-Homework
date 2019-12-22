# Import libraries
from pathlib import Path
import csv

# Set path for file
csvpath = Path("Resources/budget_data.csv")

#Declare Variables
months = 0 
net_revenue = 0
difference = 0
prior_value = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""
profits = []

# Open and read the CSV
with open(csvpath, "r") as csvfile:
    print(type(csvfile))
    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))
    header = next(csvfile)
    print(f"Header: {header}")
    row_num += 0
      
    for row in csvreader:
        print(row)
    
    # Number of Months
        months += 1
    
    # Average Change in Months
        difference = prior_value - int(row[1])
        average.append(difference)
        prior_value = int(row[1])
        average_change = sum(average) / len(average)
   
    # Find the Net Revenue    
        average_change = round(net_revenue / months, 2)
        net_revenue += int(row[1])
        
    # Find the Greatest Increase/Decrease
    if difference < greatest_increase:
        greatest_increase = difference
        greatest_increase_date = str(row[0])
    if difference > greatest_decrease:
        greatest_decrease = difference
        greatest_decrease_date = str(row[0])
        
#Print Resulting Analysis
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: ${net_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")