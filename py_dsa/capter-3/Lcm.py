# import math
#
# # Function to find LCM of two numbers
# def lcm(x, y):
#     return abs(x * y) // math.gcd(x, y)
#
# # Function to find LCM of a list of numbers
# def lcm_of_list(numbers):
#     lcm_result = 1
#     for num in numbers:
#         lcm_result = lcm(lcm_result, num)
#     return lcm_result
#
# # Example usage
# numbers = [12, 18, 24]
#
# result = lcm_of_list(numbers)
# print(f"LCM of {numbers} is {result}")


# =============================================================


import math
from functools import reduce

# Function to find LCM of a list of numbers
def lcm_of_list(numbers):
    return reduce(math.lcm, numbers)

# Example usage
numbers = [12, 18, 24]

result = lcm_of_list(numbers)
print(f"LCM of {numbers} is {result}")
