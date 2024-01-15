n = int(input("Enter the value of n: "))

result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        result -= i
    else:
        result += i

print(f"the series up to the {n}th term is: {result}")
