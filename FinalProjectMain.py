#Cesar Hernandez
#PSID 1835494

import csv
from operator import itemge

Manufacture = [] #Making blank list for manufacturing
temp_manu = []
Price = [] #Making blank list for Prices
Service = [] #Making blank list for Services
with open('ManufacturerList.csv', 'r') as f: #opening and reading lines in ManufacturerList.csv
    reader = csv.reader(f, delimiter=',')
    for line in reader:
        Manufacture.append(line)

with open('PriceList.csv', 'r') as f: #opening and reading lines in PriceList.csv
    reader2 = csv.reader(f, delimiter=',')
    for line in reader2:
        Price.append(line)

with open('ServiceDatesList.csv', 'r') as f: #opening and reading lines in ServiceList.csv
    reader3 = csv.reader(f, delimiter=',')
    for line in reader3:
        Service.append(line)

#print("orig. Man", Manufacture) #Testing manufactore list output
new_temp_manu = (sorted(temp_manu, key=itemgetter(0)))
#print(new_temp_manu)
new_manufacture = (sorted(Manufacture, key=itemgetter(0))) #sorting list by ID
#print("New: Man", new_manufacture) #Testing new manufactore list output
#print("temp manu", new_temp_manu)

#print("orig. Price", Price) #testing price list ouput
new_Price = (sorted(Price, key=itemgetter(0)))
#print("new: Price", new_Price) #testing new price list output

#print("orig Service.", Service) #testing service list output
new_Service = (sorted(Service, key=itemgetter(0)))
#print("new: Service", new_Service) #testing new service list

for x in range(len(new_manufacture)):
    del new_manufacture[x][3]
print(new_temp_manu)


for x in range(0,len(new_manufacture)):
    new_manufacture[x].append(Price[x][1])


for x in range(0,len(new_manufacture)):
    new_manufacture[x].append(Service[x][1])


print("test", new_manufacture)


Final = new_manufacture
new_Final = (sorted(Final, key=itemgetter(1)))

print("orig:", Final)
print("new:", new_Final)