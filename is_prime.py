# def is_prime(num):
#     if num % 2 or 3 == 0:
#         return "False"
#     else:
#         return "True"
# print(is_prime(3))

def is_prime(num):
    if num == 2:
        return True
    else:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
  
    return True


print(is_prime(2))