def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def count_digits(number):
    return len(str(number))

# Example: Get the factorial and count digits for the number 5
number_to_factorial = 5
result = factorial(number_to_factorial)
digit_count = count_digits(result)

print(f"The factorial of {number_to_factorial} is: {result}")
print(f"The number of digits in the factorial is: {digit_count}")
