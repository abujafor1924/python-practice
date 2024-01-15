def series_sum(n, p, terms):
    result = 0
    for k in range(1, terms + 1):
        result += n / (p ** k)
    return result

# Example usage:
n_value = 5
p_value = 2
num_terms = 4
result = series_sum(n_value, p_value, num_terms)
print(f"The sum of the series is: {result}")
