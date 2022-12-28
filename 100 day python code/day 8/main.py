# number of cans for area calculator 
# import math
# test_h = int(input("Enter the height of wall"))
# test_w = int(input("Enter the width of wall"))
# coverage =5
# def paint_calc(height,width,cover):
#     print(f"the Paint required is {math.ceil((height * width) / cover)} ") 

# paint_calc(height = test_h, width= test_w,cover= coverage)



#prime check number program 

num = int(input("Enter the number"))
def prime_check(num):
    is_prime = True
    for  i in (2, num -1):
        if num % i == 0:
            print("not a prime")
            is_prime = False
    if is_prime:
        print("it ia prime number")
    else:
        print("It is not prime number")            

prime_check(num)        
            




