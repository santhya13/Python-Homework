#Import Library
from pathlib import Path
import csv
import os

# Set path for file
csvpath = Path("Resources/budget_data.csv")

#Create Lists
net_revenue = []
monthly_changes = []
greatest_increase_month = ""
greatest_decrease_month = ""

#Initialize the Variables
months = 0
initial_value = 0
total_revenue = 0
profit_changes = 0
greatest_increase = 0
greatest_decrease = 0

# Open and Read the CSV
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        
        #Number of Months
        months += 1
        
        net_revenue.append(row[1])
        
        # Average Change in Net Revenue
        total_revenue = total_revenue + int(row[1])
        final_value = int(row[1])
        difference = final_value - initial_value
        monthly_changes.append(difference)
        profit_changes = profit_changes + difference
        initial_value = final_value
        
        # Average Change in Net Revenue Rounded
        average_change = round(profit_changes / months, 2)
        
        # Find the Greatest Increase/Decrease
        if difference > greatest_increase:
            greatest_increase = difference
            greatest_increase_month = str(row[0])
        if difference < greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_month = str(row[0])
            
#Print Resulting Analysis
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {months}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Revenue: {greatest_decrease_month} (${greatest_decrease})")