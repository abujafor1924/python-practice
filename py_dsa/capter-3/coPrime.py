import math

# def are_coprime(a, b):
#     return math.gcd(a, b) == 1
#
# # Example usage:
# num1 = 14
# num2 = 28
#
# if are_coprime(num1, num2):
#     print(f"{num1} and {num2} are coprime.")
# else:
#     print(f"{num1} and {num2} are not coprime.")


# =====================================================



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

# Example usage:
num1 = 15
num2 = 28

if are_coprime(num1, num2):
    print(f"{num1} and {num2} are coprime.")
else:
    print(f"{num1} and {num2} are not coprime.")
