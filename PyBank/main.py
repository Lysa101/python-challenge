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
    months = []
    

    for row in csvreader:
        count.append(row[0])
        monthcount=monthcount+1
      
     
#net total of profit/loss
        profit_loss.append(int(row[1]))
        total_profit_loss=int(sum(profit_loss))

    for i in range(1,len(profit_loss)):
        profit_loss_chg.append(int(profit_loss[i])-int(profit_loss[i-1]))

#average of profit/loss
    sum_profit_loss = sum(profit_loss_chg)    
    Average_change = round(sum_profit_loss/len(profit_loss_chg),2)   

#need to find the greatest increase in proft loss and corresponding month  
greatest_increase=max(profit_loss_chg)
greatest_decrease=min(profit_loss_chg)


date_increase = count[profit_loss_chg.index(greatest_increase)+1]
date_decrease = count[profit_loss_chg.index(greatest_decrease)+1]
        
print("Financial Analysis")
print("*********************")
print("Total Months:"+str(monthcount))
print("Total: $"+str(total_profit_loss))
print("Average Change: $" +str(Average_change))
print(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")

#create path for text file
textfile=os.path.join("Analysis","Financial.txt")

#open text file
file=open(textfile, "w")

#copy/write data to create the new text file
file.write("Financial Analysis")
file.write("*********************")
file.write("Total Months:"+str(monthcount))
file.write("Total: $"+str(total_profit_loss))
file.write("Average Change: $" +str(Average_change))
file.write(f"Greatest Increase in Profits: {date_increase} (${greatest_increase})")
file.write(f"Greatest Decrease in Profits: {date_decrease} (${greatest_decrease})")
