import os
import csv
with open("Resources/budget_data.csv", 'r') as budget_data:
    csv_reader=csv.reader (budget_data, delimiter=',')
# Declaration for the variable   
    months=[]
    profit_Losses=[]
    csv_header=next(csv_reader)
    monthly_change=[]
# Looping through the csv files to parse into two lists 
    for row in csv_reader:
        months.append(row[0])
        profit_Losses.append((int)(row[1]))
# caculate the net total 
        net_total=sum(profit_Losses)
# Looping through the profit_looses list to populate the variable "monthly change'
    for i in range(len(profit_Losses)-1):
        monthly_change.append(profit_Losses[i+1]-profit_Losses[i])
# Find the max and min for the monthly_change and index the row that gives the max and min 
  

     A=monthly_change.get(0)
    for X in monthly_change:
        if X >  A
        max_increase_month = X
     print(max_increase_month)
     print(monthly_change[0])
    
    
    # max_increase=max(monthly_change)
    # max_decrease=min(monthly_change)
    # max_increase_month=monthly_change.index(max_increase)+1
    # max_decrease_month=monthly_change.index(max_decrease)+1
# Print the results    
# print("Financial Analysis")
# print("--------------------------")
# print (f"Total Months:{len(months)}")
# print (f"Total: $ {net_total}")
# print (f"Average  Change: ${round(sum(monthly_change)/(len(profit_Losses)-1),2)}")
# print(f"Greatest Increase in Profits: {months [max_increase_month]}(${max_increase})")
# print(f"Greatest Decrease in Profits: {months [max_decrease_month]}(${max_decrease})")

