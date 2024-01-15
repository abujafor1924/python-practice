# def extended_gcd(a, b):  # (a * x) % m = 1
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x
#
#
# def mod_inverse(a, m):
#     gcd, x, y = extended_gcd(a, m)
#     if gcd != 1:
#         raise ValueError(f"The modular inverse does not exist for {a} modulo {m}")
#     else:
#         return x % m
#
#
# # Example
# a = 3
# m = 11
# inverse = mod_inverse(a, m)
#
# print(f"The modular inverse of {a} modulo {m} is: {inverse}")

# =====================================================


def mod_inverse(a, m):
    # pow(a, b, m)
    # a * x % m = 1
    # a ** b % m
    return pow(a, -1, m)

# Example
a = 3
m = 11
inverse = mod_inverse(a, m)

print(f"The modular inverse of {a} modulo {m} is: {inverse}")
