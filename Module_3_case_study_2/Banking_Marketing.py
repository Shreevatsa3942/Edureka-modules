

import csv

result = []
job_list=[]
with open('bank-data.csv','r') as file:
  csv_reader=csv.reader(file)
  fields = next(csv_reader)
  for row in csv_reader:
    result.append(row[1])

#finding distinct elements
[job_list.append(x.strip()) for x in result if x not in job_list]
#print(job_list)

try:
  profession=input("Enter the Profession :")
  if profession in job_list:
    print("Client is Eligible to apply:")
  else:
    raise Exception("Client is not Eligible to apply for a job")
except Exception as e:
  print(e)

