# final file

import os
import csv

c_csv = os.path.join("employee_data.csv")

csv_list = []
with open(c_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        csv_list.append(row)


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


new_emp_list = list()

for emp in csv_list:
    new_emp = [emp[0], emp[1].split(' ')[0], emp[1].split(' ')[1], emp[2], emp[3], emp[4]]
    new_emp[3] = new_emp[3][-5:] + "-" + new_emp[3][:4]   
    new_emp[4]= "***-**-" + new_emp[4][-4:]
    new_emp[5] = us_state_abbrev[new_emp[5]]
    new_emp_list.append(new_emp)

    
with open('solution_data.csv', 'w') as csvfileWrite:
    fieldnames = ['Emp ID', 'First Name', 'Last Name','DOB','SSN','State']
    writer = csv.DictWriter(csvfileWrite, fieldnames=fieldnames)

    writer.writeheader()
    
    for emp in new_emp_list:
        writer.writerow({'Emp ID': emp[0], 'First Name': emp[1], 'Last Name': emp[2], 'DOB':emp[3], 'SSN':emp[4], 'State': emp[5]})

