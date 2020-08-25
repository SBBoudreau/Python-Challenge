#Import budget_data.csv
import csv
import os

#name variales

Total_Months = 0
Net_Total = 0
Average_Change = 0
Net_Change_List = []
Previous_Net = 0
Greatest_Increase = ["",0]
Greatest_Decrease = ["",99999999999999999999]

#import csv 

import_csv_file = os.path.join("Resources", "budget_data.csv")

#read csv & skip header row

with open(import_csv_file, "r") as data:
    csvreader = csv.reader(data)
    header_row = next(csvreader)

    First_Data_Row = next(csvreader)
    Total_Months = 1 
    Net_Total = int(First_Data_Row[1])
    Previous_Net = Net_Total   

#calculations

    for row in csvreader:
        Total_Months = Total_Months + 1
        Net_Total  = Net_Total + int(row[1])
        Net_Change = int(row[1]) - Previous_Net
        Previous_Net = int(row[1])
        Net_Change_List.append(Net_Change)

        if Net_Change > Greatest_Increase[1]:
            Greatest_Increase[0] = row[0]
            Greatest_Increase[1] = Net_Change

        if Net_Change < Greatest_Decrease[1]:
            Greatest_Decrease[0] = row[0]
            Greatest_Decrease[1] = Net_Change

Average_Change = sum(Net_Change_List)/len(Net_Change_List) 

#export & format text file to show results

export_text_file = os.path.join("Analysis", "Financial_Analysis.txt")


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Total: ${Net_Total}\n"
    f"Average  Change: ${Average_Change}\n"
    f"Greatest Increase in Profits: {Greatest_Increase[0]} (${Greatest_Increase[1]})\n"
    f"Greatest Decrease in Profits: {Greatest_Decrease[0]} (${Greatest_Decrease[1]})\n"    
)
print(output)
with open(export_text_file, "w") as text_file:
    text_file.write(output)



