import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

#assign data fields/variables/dictionary
votes=0
vote_percentage = []
winner=[]
candidatedict = [{"Khan": 0,"Correy": 0,"Li": 0,"O_Tooley": 0}]
#votes.append=candidatedict + 1
total_votes=int(votes)
    

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)
    #print(csvheader)

#tally votes for candidates
    for candidate in csvreader:
        total_votes=total_votes + 1
        if candidate [2] =="Khan":
            Khan = Khan + 1

        elif candidate [2] == "Correy":
            Correy = Correy + 1
        
        elif candidate [2] == "Li":
            Li = Li + 1

        elif candidate [2] == "O_Tooley":
            O_Tooley = O_Tooley

               #votes +=1
    
    print("Election Results")
    print("******************")
    print("Total Votes:")
    print("*******************")
    print("Khan:")
    print("Correy:")
    print("Li:")
    print("O'Tooley:")
    print("********************")
    print("Winner:")
    print("********************")

   
    #total number of votes
    
    
    #for row in(csvreader):
        #votes =+1

        #if candidate in candidatedict:
            #{"Khan":votes,
            #"Li":votes,
            #"Correy":votes,
            #"O_Tooley": votes}
        
        
        

        #total_votes.append(int(row[1]))
    
    #print(total_votes)
    #newfile = os.path.join("Resources","Election stats.txt")
    #file("Election stats.txt", "w")
    #file.write("Election Results")
    #file.write("******************")
    #file.write("Total Votes:")
    #file.write("*******************")
    #file.write("Khan:")
    #file.write("Correy:")
    #file.write("Li:")
    #file.write("O'Tooley:")
    #file.write("********************")
    #file.write("Winner:")
    #file.write("********************")