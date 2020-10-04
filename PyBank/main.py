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
    profit_loss_chg =[]
    months=[]
    

    for row in csvreader:
        count.append(row[0])
        monthcount=monthcount+1
      
     
#net total of profit/loss
        profit_loss.append(int(row[1]))
        total_profit_loss=int(sum(profit_loss))

    for i in range(1,len(profit_loss)):
        profit_loss_chg.append(int(profit_loss[i])-int(profit_loss[i-1]))

        
    Total_Months=len(months)   
#greatest_increase=max
#greatest_decrease=min
    #print(total_profit_loss)
    #print(monthcount)
    
#average of profit/loss
#from statistics import mean
#def Average(profit_loss):
    #return mean(profit_loss)
#average=Average(profit_loss)
#print(average)

#greatest increase in profit/loss
#need month of greatest increase 
#need to find the greatest increase in proft loss and corresponding month
#date[]

#if profit_loss==max(profit_loss):
    #max(row(greatest_increase))
#elif profit_loss==min(profit_loss):
    #min(row(greatest_decrease))         


   
    


#min=min(total_profit_loss)
#print(min)

#greatest decrease in profit/loss

print("Financial Analysis")
print("*********************")
print("Total Months:"+str(monthcount))
print("Total: $"+str(total_profit_loss))
#print("Average Change: $" +(average))
print("Greatest Increase in Profits: $")
print("Greatest Decrease in Profits: $")




