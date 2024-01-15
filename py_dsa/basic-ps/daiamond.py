def print_diamond_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * (2 * i + 1))

    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1), end="")
        print("*" * (2 * i + 1))


diamond_size = int(input("Enter your daimond number : "))
print_diamond_pattern(diamond_size)
