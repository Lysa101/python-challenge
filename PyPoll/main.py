import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#assign data fields/variables/dictionary

total_votes = 0
vote_percentage = []
winner = []
Khan = 0
Correy =  0 
Li = 0 
O_Tooley = 0
    
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)
    #print(csvheader)


#tally votes for candidates
    for candidate in csvreader:
       
        total_votes = total_votes + 1
        if candidate [2] =="Khan":
            Khan = Khan + 1

        elif candidate [2] == "Correy":
            Correy = Correy + 1
        
        elif candidate [2] == "Li":
            Li = Li + 1

        else: 
            O_Tooley = O_Tooley + 1

    #calculate % of votes per candidate

    kpercent = round((Khan / total_votes),2)
    cpercent = round((Correy / total_votes),2)
    lpercent = round((Li / total_votes),2)
    tpercent = round((O_Tooley / total_votes),2)
    
    #to determine winner
    Winner = max(Khan,Correy,Li,O_Tooley)

    if Winner == Khan:
        Winner = "Khan"
        
    elif Winner == Correy:
            Winner = "Correy"

    elif Winner == Li:
            Winner = "Li"

    else:
            Winner = "O_Tooley"


    print("Election Results")
    print("******************")
    print("Total Votes:"+str(total_votes))
    print("*******************")
    print(f"Khan : {kpercent:.2%} ({Khan})")
    print(f"Correy :{cpercent: 2%} ({Correy})")
    print(f"Li : {lpercent:.2%} ({Li})")
    print(f"O_Tooley : {tpercent:.2%} ({O_Tooley})")
    print("********************")
    print(f"Winner: {Winner}")                  
    print("********************")

          
    #create a text file and path   
    
    newfile = os.path.join("Analysis","Election stats.txt")
    file = open(newfile, "w")

    #copy or write data to new file

    file.write("Election Results")
    file.write("******************")
    file.write("Total Votes:"+str(total_votes))
    file.write("*******************")
    file.write(f"Khan : {kpercent:.2%} ({Khan})")
    file.write(f"Correy :{cpercent: 2%} ({Correy})")
    file.write(f"Li : {lpercent:.2%} ({Li})")
    file.write(f"O_Tooley : {tpercent:.2%} ({O_Tooley})")
    file.write("********************")
    file.write(f"Winner: {Winner}")                  
    