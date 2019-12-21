# Import libraries
from pathlib import Path
import csv

# Set path for file
csvpath = Path("Resources/budget_data.csv")

#Declare Variables
months = 0 
net_revenue = 0
prior_value = 0
average_change = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

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
    # Average Change in Months
        difference = prior_value - int(row[1])
        average.append(difference)
        prior_value = int(row[1])
        average_change = sum(average) / len(average)
    # Find the Net Revenue    
        net_revenue = int(row[1])
        
#Print Resulting Analysis
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${net_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")