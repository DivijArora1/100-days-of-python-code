def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2
operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}
def calculator():
    num1 = float(input("Enter the 1st number: "))
    for symbol in operations:
            print(symbol)
    should_continue = True

    while should_continue:

        operations_symbol = input("Pick the  operation: ")        
        num2 = float(input("Enter the 2nd number: "))
        calculation_functions = operations[operations_symbol] 
        answer = calculation_functions(num1,num2)

        print(f"{num1} {operations_symbol} {num2} = {answer} ") 
        if input(f"type y to continue calculating with ans or n to exit") =='y':
            num1 = answer
        else:   
            should_continue = False
            calculator()

calculator()

