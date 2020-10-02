import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)

    #assign of data 
    votes.append=(candidate[0])
    candidatedict = {"Khan","Correy","Li","O_Tooley"}
    total_votes=(len(votes)
    candidate=(candidatedict[2])
    vote_percentage = []
    winner=[]
   
    #total number of votes
    
    
    for row in(csvreader):
        votes =+1

        if candidate in candidatedict:
            {"Khan":votes,
            "Li":votes,
            "Correy":votes,
            "O_Tooley": votes}
        
        
        

        total_votes.append(int(row[1])
    
    #print(total_votes)