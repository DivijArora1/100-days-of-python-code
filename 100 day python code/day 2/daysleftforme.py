from math import floor


age = int(input("Enter youur age : \n"))
days = 365*90
weeks = 90*52
months = 12*90
years = 90

daysLeft = days - age*365 
weeksLeft = weeks - age*52
monthsLeft = months - age*12 
yearsLeft = years - age 

print(f" you have {daysLeft} days , {weeksLeft} weeks  {monthsLeft}months and {yearsLeft} years left ")



