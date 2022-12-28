print("welcome to python pizza delivery")
size= input("What size of pizza do you want ? s,m,l : \n ")
add_pepperoni = input("Do you want to add pepperoni to it ? y,n : \n")
extra_cheese = input("Do you want to add extra to it ? y,n : \n")
pizza =0
if size =='s':
    pizza = 15
elif size =='m':
    pizza = 20
else:
    pizza = 25

if add_pepperoni == 'y' and size=='s':
    pizza +=2
elif add_pepperoni=='y' and size=='m':
    pizza +=3    
elif add_pepperoni=='y' and size=='l':
    pizza +=3    
else:
    pizza +=0    

if extra_cheese =='y':
    pizza +=1
else:
    pizza +=0

print(f"The total of your order is {pizza}$")



