# def my_function():
#     for i in range(1,20):
#         if i ==10:
#             print("You got it")
#         print(i)    
#         i+=1        
# my_function()        

from random import randint
dice_imgs = ["O","O","O","O","O","O"]
dice_num = randint(1,6) #included 1 and 6 so will cause error
print(dice_imgs[dice_num])
 

# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page =int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item) 
#     print(b_list)   
# mutate([1,2,4,5,6,7,8])    



# number = int(input("Which number do you want to check"))
# if number % 2 == 0:
#     print("It is an even number")
# else:
#     print("It is an odd number")    



# for number in range(1,100):
#     if number % 3 == 0 and number % 5 ==0:
#         print("FizzBuzz")
#     elif number % 3 ==0:
#         print("Fizz")    
#     elif number % 5 ==0:
#         print("Buzz")    
#     else:
#         print(number)    







