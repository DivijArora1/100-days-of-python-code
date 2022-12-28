import pandas

data = pandas.read_csv("day 25\weatherdata.csv")
# print(type(data)) #data frame
# print(data["temp"])  #takes column row name
# print(type(data["temp"]))  #series

#full data table in the data sheet is a data frame in pandas and the singel column is the series in pandas


#dataframe to disctionary
data_dict = data.to_dict()
# print(data_dict)

#series to list
temp_list = data["temp"].to_list()
# print(temp_list)

#find avg of the list of temp
average = sum(temp_list)/len(temp_list)
# print(average)
#same using pandas
# print(data['temp'].mean())

#getting hold of highest value
highest_value = data["temp"].max()
# print(highest_value)


#data["condition"] is simmilar to data.condition


#getting data in row
# print(data[data.day == "Monday"])

#getting th row which has highest temp in the row
# print(data[data.temp == data["temp"].max() ])

#getting condtion of a particular data
monday = data[data.day=="Monday"]
# print(monday.conditi  on)
# print(monday.temp)
 
#  °F = (°C × 9/5) + 32
fareheight = monday.temp * 9/5 + 32
# print(fareheight)

#creating a dataframe from scratch

data_dictionary = {
    "students" : ["Amy" , "James" , "Angela"],
    "scores"  : [56,78,90]
}
data = pandas.DataFrame(data_dictionary)

print(data)
# data.to_csv("new_data.csv")












