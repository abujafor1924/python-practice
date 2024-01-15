# def small_to_large(a, b, c):
#     storet_number = sorted([a, b, c])
#     return storet_number
#
#
# x, y, z = map(int, input("Enter Your Three Number : ").split())
# result = small_to_large(x, y, z)
# print(result)

# =========================================================

# def small_to_large(*args):  # Unlimited input by args method
#     sorted_numbers = sorted(args)
#     return sorted_numbers
#
# # Example usage
# user_input = input("Enter Your Numbers separated by space: ")
# numbers = map(int, user_input.split())
# result = small_to_large(*numbers)
# print(result)

# ==================================================


def bubble_sort(*numbers):
    numbers = list(numbers)
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


# Example usage:
input_numbers = map(int, input("Enter your Numbers separated by space: ").split())
sorted_numbers = bubble_sort(*input_numbers)

print("Sorted array:", sorted_numbers)
