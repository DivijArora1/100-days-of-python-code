import pandas


data = pandas.read_csv("day 25\squirrel data\squirrels_data.csv")
grey_suirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_suirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_suirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_suirrels_count)
# print(red_suirrels_count)
# print(black_suirrels_count)


data_dict ={
    "Fur Color" : ["Gray", "Cinnamon" , "Black"],
    "Count " : [grey_suirrels_count,red_suirrels_count,black_suirrels_count]
}

df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
