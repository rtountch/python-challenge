#final file

import os
import csv


c_csv = os.path.join("budget_data.csv")

lines = []

with open(c_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    NumMonths = 0 # variable to hold the # of months
    TotalProfitLoss = 0 # variable to hold the total Profit / Loss
    AvgProfitLoss = 0 # variable to hold the average Profit / Loss over the period
    
    MaxProfit = 0
    MinLoss = 0
    
    MaxDate = "Jan-2010"
    MinDate = "Jan-2010"
    
    
    for row in csvreader:
        
        NumMonths = NumMonths + 1

        Amount = int(row[1])
        TotalProfitLoss = TotalProfitLoss + Amount
        
        if MaxProfit < Amount:
            MaxProfit = Amount
            MaxDate = row[0]
        
        if MinLoss > Amount:
            MinLoss = Amount
            MinDate = row[0]

    
    AvgProfitLoss = TotalProfitLoss / NumMonths
    
    lines.append("There are a total of "+ str(NumMonths) + "months in this data set")
    print("There are a total of ", NumMonths, "months in this data set")
    
    lines.append("The total Profit / Loss over the period is $" + str(TotalProfitLoss))
    print("The total Profit / Loss over the period is $",TotalProfitLoss)
    
    lines.append("The average monthly Profit / Loss is $" + str("%.2f" % AvgProfitLoss))
    print("The average monthly Profit / Loss is $", "%.2f" % AvgProfitLoss)
    
    lines.append("The Max Profit is $" + str(MaxProfit) + " " + MaxDate)
    print("The Max Profit is $" + str(MaxProfit)+ " " + MaxDate)
    
    lines.append("The Min Profit is $" + str(MinLoss)+ " " + MinDate)
    print("The Min Profit is $" + str(MinLoss)+ " " + MinDate)
    

with open('solution_data.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(lines))