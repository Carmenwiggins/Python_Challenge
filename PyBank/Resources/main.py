import os
import csv

budget_data_csv=os.path.join("..","Resources","budget_data.csv")
                             
#sheet = csv.DictReader(CoData)

Total_profit_Losses = 0
months = 0
Previous_Profit_Losses = 0
Current_Profit_Losses = 0
output_file = "analysis.txt"

Change_in_Profit_Losses =[] 

max_profit = float('-inf')
min_profit = float('inf')
max_profit_month= " "
min_profit_month = " "
with open("budget_data.csv")as csvfile:
    Sheet = csv.DictReader(csvfile,delimiter=",")
                           
    for row in Sheet:
  
        Total_profit_Losses = Total_profit_Losses + int(row['Profit/Losses'])
        months = months + 1

        if months > 1:
            Current_Profit_Losses = int(row['Profit/Losses'])
            Current_Change = Current_Profit_Losses- Previous_Profit_Losses
            Change_in_Profit_Losses.append(Current_Change)
            
            Previous_Profit_Losses= int(row['Profit/Losses'])
            if max_profit< Current_Change:
                 max_profit=Current_Change
                 max_profit_month= row["Date"]
                 
            if min_profit> Current_Change:
                 min_profit=Current_Change
                 min_profit_month= row["Date"]
        else:
           Previous_Profit_Losses= int(row['Profit/Losses'])  
#Calculate the change of profit and losses and min and max

Average_Change = sum (Change_in_Profit_Losses) / len(Change_in_Profit_Losses)


# to print analysis to the terminal and export a text file 
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print("Total Months:", months) 
print("Total Profit/Losses: $",Total_profit_Losses)
print("Average Change $",Average_Change)
print("Greatest Increase in Profit:", max_profit_month,"(${:.2f}".format(max_profit))   
print("Greatest Decrease in Profit:", min_profit_month, "(${:.2f}".format(min_profit)) 
#--------------------------------------------------------------------
# Open the output file and write the analysis
with open(output_file, "w") as file:
    
        file.write("Total Months: {}\n".format(months))
        file.write("Total Profit/Losses: ${}\n".format(Total_profit_Losses))
        file.write("Average Change: ${}\n".format(Average_Change))
        file.write("Greatest Increase in Profit: {} (${:.2f})\n".format(max_profit_month, max_profit))
        file.write("Greatest Decrease in Profit: {} (${:.2f})\n".format(min_profit_month, min_profit))



