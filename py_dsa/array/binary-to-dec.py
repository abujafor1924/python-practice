# Binary array input
binary_array = [1, 0, 1, 1, 0, 1]

# Convert binary array to decimal
decimal_number = int("".join(map(str, binary_array)), 2)

# Print the result
print(f"The decimal representation is: {decimal_number}")
