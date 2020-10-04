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

    #print(total_profit_loss)
    #print(monthcount)
    
#average of profit/loss

#greatest increase in profit/loss
#greatest decrease in profit/loss

print("Financial Analysis")
print("*********************")
print("Total Months:"+str(monthcount))
print("Total: $"+str(total_profit_loss))
print("Avergage Change: $")
print("Greatest Increase in Profits: $")
print("Greatest Decrease in Profits: $")




