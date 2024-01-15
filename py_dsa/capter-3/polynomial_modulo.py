def polynomial_modulo(a, b, m):
    result = 0
    power_of_a = 1

    for i in range(b):
        result = (result + (i + 1) * power_of_a) % m
        power_of_a = (power_of_a * a) % m

    return result

# Example usage:
a = 2
b = 5
m = 1000000007  # Replace with your desired modulo value

result_mod_m = polynomial_modulo(a, b, m)
print(result_mod_m)
