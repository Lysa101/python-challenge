import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)

    profit_loss=[]
    count=[]
    monthcount=0

    for row in csvreader:
        count.append(row[0])
        monthcount=monthcount+1
 
#net total of profit/loss
        profit_loss.append(int(row[1]))
        total_profit_loss=int(sum(profit_loss))

    print(total_profit_loss)
    print(monthcount)
    
