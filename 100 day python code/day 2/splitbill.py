bill = int(input("Enter your total bill amount: \n"))
tip = int(input("Enter the percentage of tip you would like to give: \n"))
ppBill = int(input("Enter the no. of persons you like to split: \n"))

tipPercentage = bill*tip/100
grandTotal = bill + tipPercentage
eachShare = round(grandTotal/ppBill ,2)
print(f"The share of each person is {eachShare}: \n")
