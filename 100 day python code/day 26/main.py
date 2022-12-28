# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)    
# print(new_list)

#using list comprihention
# new_list = [n + 1 for n in numbers]
# print(new_list)


# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)


#multiply each number
# new_list = [n*2 for n in range(1,5)]
# print(new_list)


names = ["alex","betty","Yug","divij","sim"]
# new_list = [name for name in names if len(name)<5]
# print(new_list)
new_list = [name.upper() for name in names  if len(name)<7  ]
print(new_list)
