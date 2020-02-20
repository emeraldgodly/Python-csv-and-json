
import json
import csv


with open('test_data.json') as json_file:
    data = json.load(json_file)

product_data = data['prdt_details']


data_file = open('new_data_file.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for emp in product_data:
    if count == 0:

        header = emp.keys()
        csv_writer.writerow(header)
        count += 1

    csv_writer.writerow(emp.values())

data_file.close()


###################################################################################

import csv
exampleFile = open('new_data_file.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)

for i in range(3,199):
    if i % 2 == 0:
        print(exampleData[i][5])
        print(type(exampleData[i][5]))


