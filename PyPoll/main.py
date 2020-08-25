#Import election_data.csv
import csv
import os

Total_Votes = 0
candidate = []
percentage = []
candidate_votes = {}

import_csv_file = os.path.join("Resources", "election_data.csv")

with open(import_csv_file, "r") as data:
    csvreader = csv.reader(data)
    header_row = next(csvreader)

    for x in csvreader:
        Total_Votes = Total_Votes + 1
            
        candidate = x[2]
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1  

for key in candidate_votes.keys():
    if candidate_votes[key] == max(candidate_votes.values()):
        winner = key 

          

print("Election Results")
print("------------------------")
print(f"Total Votes: {Total_Votes}")    
print("------------------------")
for i in candidate_votes:
    percentage = round((float(candidate_votes[i])/Total_Votes)*100, 2)
    print(f"{i} {percentage}% ({candidate_votes[i]})")
print("------------------------")
print(f"Winner: {winner}")   
print("------------------------")   

export_text_file = os.path.join("Analysis", "Election_Results.txt")
with open(export_text_file, "w") as text_file:
    text_file.write("Election Results""\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Votes: {Total_Votes}\n")    
    text_file.write("------------------------")
    text_file.write("\n")
    for i in candidate_votes:
        percentage = round((float(candidate_votes[i])/Total_Votes)*100, 2)
        text_file.write(f"{i} {percentage}% ({candidate_votes[i]})\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("------------------------")


