def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


input_number = int(input("Enter a Number : "))
result = factorize(input_number)
print(f"The Factor of {input_number} are : {result}")
