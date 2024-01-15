def count_consecutive_ones(binary_string):
    max_count = 0
    current_count = 0

    for digit in binary_string:
        if digit == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Example usage:
binary_string = "101110111100"
result = count_consecutive_ones(binary_string)
print(f"The maximum consecutive sequence of ones is: {result}")
