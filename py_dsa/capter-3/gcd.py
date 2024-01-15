def gcd(a, b):
    while b:
        a, b = b, a % b  # swaping system

        # temp = a
        # a = b
        # b = temp % b
    return a


# Example usage:
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")
