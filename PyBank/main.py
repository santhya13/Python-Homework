#Import Libraries
from pathlib import Path
import csv

#Set File Path
csvpath = Path("Resources/budget_data.csv")

#Initialize Variables
mouth_count = 0
net_revenue = 0
average_change = 0

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
    
#Print Resulting Analysis
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${net_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")