from doctest import OutputChecker
import os
import csv
file = os.path.join('..', 'python challenge' 'Resources','BudgetData.csv')
with open('BudgetData.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next (csvreader)
    #lists that will have the csv values 
    month_count = []
    profit = []
    change_profit = []


    #values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i]) 

#the max and min from the list that was made
increase = max(change_profit)  
decrease = min(change_profit)

#utlizing the index,
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print (f"Average Change: {round(sum(change_profit)/len(change_profit), 2)}")
print (f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print (f"Greatest Deccrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")


output= OutputChecker.txt
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months: {len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Chnage: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${str(decrease)})")