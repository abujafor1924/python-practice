def sum_of_integers(n):
    # Ensure that the input is within the specified range
    if abs(n) > 10000:
        return "Input should not be greater than 10000 by its absolute value."

    # Calculate the sum of integers from 1 to N
    if n >= 1:
        result = (n * (n + 1)) // 2
    else:
        result = (-n * (n + 1)) // 2

    return result

# Get input from the user
N = int(input("Enter the value of N: "))

# Calculate and print the sum of integers
print("Sum of integers from 1 to", N, "is:", sum_of_integers(N))
