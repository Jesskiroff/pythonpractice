def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dic = {}
calc_dic["+"] = add
calc_dic["-"] = subtract
calc_dic["*"] = multiply
calc_dic["/"] = divide

print(calc_dic["*"](n1=4, n2=8))

