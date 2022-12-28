# fruits = ["Mango","Apple", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Juice")

'''avg height without len or sum'''
# student_heights =  input("input a list of students height").split()
# print(student_heights) #--list as str
# for n in range(0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights) #--list as int

# total_height = 0
# for height in student_heights:
#     total_height += height
# # print(total_height)   

# number_of_students = 0
# for students in student_heights:
#     number_of_students += 1
# # print(number_of_students)
# print(total_height/number_of_students)


''' high score '''
# student_score =  input("input a list of students score").split()

# for n in range(0,len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)

# highest_score = 0
# for score in student_score:
#     if score > highest_score:
#         highest_score = score

# print(f"The highest score is {highest_score} ")

# total of all even numbers 
# total = 0
# for i in range(1,101):
#    if i%2 ==0:
#     total = total + i

# print(total)







# for i in range(1,101):
#     # print(i) 
#     if i%3 ==0:
#         print("Fizz")
#     elif i%5 ==0:
#         print("Buzz") 
#     elif i%15==15:
#         print("FizzBuzz")  
#     else:
#         print(i)    
            




# PASSWORD GENERATOR
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# # easy
# password =""
# for char in range(1,nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char

# for char in range(1,nr_symbols + 1):
#     random_char = random.choice(symbols)
#     password += random_char

# for char in range(1,nr_numbers + 1):
#     random_char = random.choice(numbers)
#     password += random_char
# print(password)



# hard
password_list =[]
for char in range(1,nr_letters + 1):
    password_list.append(random.choice(letters))
     

for char in range(1,nr_symbols + 1):
    password_list.append(random.choice(symbols))
     

for char in range(1,nr_numbers + 1):
    password_list.append(random.choice(numbers))
     
random.shuffle(password_list)     
print(password_list)

password=''
for char in password_list:
    password += char
print(password)    












