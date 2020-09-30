import os
import csv
csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath, 'r') as file_handler:
     lines = file_handler.read()
     print(lines)
     print(type(lines))

mylist = ['Date','Profit/Losses']
print(mylist)

#for row in open ('budget_data.csv'):
    #num_rows += 1
    #print(num_rows)
#mylist=['Date','Profit/Losses']
Months_count = mylist.count('Date')
print('Total Months': Months_count) 
