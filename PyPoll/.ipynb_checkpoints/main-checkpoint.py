# the final code

import os
import csv

c_csv = os.path.join("election_data.csv")
#print(c_csv)

csv_list = []
with open(c_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        csv_list.append(row)

    
Candidates = list() # a list to contain the list of candidates and relevant statistics

# print("I am here")
for row in csv_list:
    
    unique = "y"
    unique_record = []
    
    for j in Candidates:
        if j[0] == row[2]:
            unique = "n"
            j[1]=j[1]+1
            j[2]=round(j[1]/len(csv_list),2)
    
    if unique == "y":
        unique_record = [row[2],1,0] # candidate name, total votes, % votes
        Candidates.append(unique_record)
     
lines = []
    
lines.append("Election Results")
print("Election Results")

lines.append("------------------------------")
print("------------------------------") 

lines.append("Total Votes" + str(len(csv_list)))
print("Total Votes", len(csv_list))

lines.append("------------------------------")
print("------------------------------") 


Winner = Candidates[0]

for c in Candidates:
    new_line = c[0]+":"+ "      \t"+ str("{0:.0%}".format(c[2]))+ "\t"+ "("+ str(c[1])+")"
    print(new_line)
    lines.append(new_line)
    #print(c[0],":", "   \t", "{0:.0%}".format(c[2]), "\t", "(", c[1],")")
    if(c[2] > Winner[2]):
        Winner = c

lines.append("------------------------------")       
print("------------------------------") 

lines.append("Winner: " + Winner[0])
print("Winner: ",Winner[0])

lines.append("------------------------------")  
print("------------------------------") 



with open('solution_data.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(lines))
    