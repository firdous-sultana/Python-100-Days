from art import logo
print(logo)

#addition
def add(n1, n2):
    return n1 + n2

#subtraction
def subtract(n1, n2):
    return n1 - n2

#multiplication
def multiply(n1, n2):
    return n1 * n2

#division
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    num1 = int(input("What is the first number?"))
    for operators in operations:
            print(operators)

    flag = True
    while flag:
        num2 = int(input("What is the next number?"))
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print("{} {} {} = {}".format(num1, operation_symbol, num2, answer))

        continue_ = input("Type 'y' to continue calculating with the {} or type 'n' to start a new calculation ".format(answer))
        if(continue_ == 'y'):
            num1 = answer
        else:
            flag = False
            calculator()

calculator()