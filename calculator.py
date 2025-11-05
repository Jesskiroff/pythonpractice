def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide

print(operations["*"](n1=4, n2=8))

num1 = float(input("What is the first number?: "))
operation_symbol = input("Pick an operation: +, -, *, or / ")
num2 = float(input("What is the next number?: "))

print(operations[operation_symbol](num1, num2))

