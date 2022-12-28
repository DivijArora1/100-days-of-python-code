# with open("day 25\weatherdata.csv" , mode = "r") as data:
#     content = data.readlines()
#     print(content)

#comma seperated values

import csv

with open("day 25\weatherdata.csv") as data_file:
    data = csv.reader(data_file)#will create a object
    temperatures = []    
    for row in data:# seperate each line with a list
        # print(row)
        # print(row[1]) #but this prints the temp(lable) at top
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
#this procedure is so difficult ..that is why pandas are intrroduced
#data analysis 


