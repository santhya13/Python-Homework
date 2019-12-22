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
profit = []

# Open and read the CSV
with open(csvpath, "r") as csvfile:
    print(type(csvfile))
    csvreader = csv.reader(csvfile, delimiter=',')
    print(type(csvreader))
    header = next(csvfile)
    print(f"Header: {header}")
      
    for row in csvreader:
        print(row)
    
        # Number of Months
        months += 1
    
        # Average Change in Months
        profit.append(difference)
        difference = prior_value - int(row[1])
        prior_value = int(row[1])
    
        # Find the Net Revenue    
        net_revenue += int(row[1])
        average_change = round(net_revenue / months, 2)
        
        # Find the Greatest Increase/Decrease
        if difference < greatest_increase:
            greatest_increase = difference
            greatest_increase_month = str(row[0])
        elif difference > greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_month = str(row[0])
        
#Print Resulting Analysis
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: ${net_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")