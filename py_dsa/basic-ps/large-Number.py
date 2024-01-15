def large_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


x, y, z = map(float, input("Enter your Three Number : ").split())
result = large_number(x, y, z)
print(result)
