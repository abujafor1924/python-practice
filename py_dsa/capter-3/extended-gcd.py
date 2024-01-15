def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Example usage:
a = 48
b = 18
gcd, x, y = extended_gcd(a, b)

print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients (x, y) in Bézout's identity: {x}, {y}")
