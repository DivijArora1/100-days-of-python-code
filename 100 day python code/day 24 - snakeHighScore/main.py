# file  = open("day 24\my_file.txt")
# contents = file.read()
# print(contents)
# file.close()#as python uses resourses to open file ..so we need to close it..so it does not put burden on our computer

#different way of opening file
# with open("day 24\my_file.txt") as file:
#     content = file.read()
#     print(content)#no need to close

#to write in file    
# with open("day 24\my_file.txt",mode='w') as file:
#     file.write("hello divij") #replace all text
# if file is not present it will create a new file 
# bydefault mode is 'r'--read

#to append in file    
with open("day 24\my_file.txt",mode='a') as file:
    file.write("hello angela") 
    




