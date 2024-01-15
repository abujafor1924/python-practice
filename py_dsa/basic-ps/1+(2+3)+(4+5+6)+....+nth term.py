n = int(input("Enter the value of n: "))

sum = 0
term = 1

for i in range(1, n + 1):
    group_sum = 0

    for j in range(1, i + 1):
        group_sum += term
        term += 1

    sum += group_sum

print("Sum of the series:", sum)
