import random

name_str = input("enter names")
names = name_str.split(", ")

num_items = len(names)
random_choice = random.randint( 0, num_items -1)

random_mealBuyer = names[random_choice]

print(random_mealBuyer+ "Is going to pay the bill")

