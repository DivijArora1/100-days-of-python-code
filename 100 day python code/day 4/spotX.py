row1 = ["😁","😁","😁"]
row2 = ["😁","😁","😁"]
row3 = ["😁","😁","😁"]
map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")

position = input("where do you want to put the treasure: ") #23
vertical = int(position[0]) #2
horizontal = int(position[1]) #3
selected_row = map[vertical -1] #yaha pr row save hogyi
selected_row[horizontal -1] = "X" #ab uss row ka item replace hoga

print(f"{row1}\n{row2}\n{row3}")





