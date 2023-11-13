import os
import csv

#election_data = os.path.join("Resources/election_data.csv")
#election_data = os.path.join("Challenge_Homework/Python_Challenge/PyPoll/Resources/election_data.csv")
election_data = os.path.join("PyPoll/Resources/election_data.csv")
with open(election_data) as sheet:
    csvreader = csv.reader(sheet, delimiter=",")

    Total_Votes = 0
    Candidate = {}
    output_file = os.path.join("PyPoll/Analysis/analysis.txt")

    for row in csvreader:
        Total_Votes += 1

        # Get candidate name 
        candidate_name = row[2]  

        if candidate_name in Candidate:
            Candidate[candidate_name] += 1
        else:
            Candidate[candidate_name] = 1

# Print results
print("Election Results")
print("-------------------------")
print("Total Votes:", Total_Votes)
print("-------------------------")

# Print results for each candidate
for candidate, votes in Candidate.items():
    percentage = (votes / Total_Votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Find the winner
winner = max(Candidate, key=Candidate.get)
print("-------------------------")
print("Winner Is:", winner)
print("-------------------------")

with open(output_file, "w") as file:
    
        
    file.write("Total Votes: {}\n".format(Total_Votes))
    for candidate, votes in Candidate.items():
        percentage = (votes / Total_Votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("winner: {}".format(winner))   



    
    


   
  
