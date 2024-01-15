def bigmod(a, b, m): # (a*b)%c = ((a%c)*(b%c))%c big mod sutro
    if b == 0:
        return 1 % m
    elif b % 2 == 0:
        half_result = bigmod(a, b // 2, m)
        return (half_result * half_result) % m
    else:
        return (a * bigmod(a, b - 1, m)) % m   # recursive function
# Example usage:
a = 5
b = 3
m = 13
result = bigmod(a, b, m)
print(f"{a}^{b} % {m} = {result}")
