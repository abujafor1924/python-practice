# def analyze_number(anita):
#     basic_numbers = [2, 3, 5, 7, 11]  # You can add more basic numbers as needed
#
#     results = {}
#
#     for divisor in basic_numbers:
#         if anita % divisor == 0:
#             results[divisor] = True
#         else:
#             results[divisor] = False
#
#     return results
#
#
# # Example usage
# anita = 30  # You can replace this with the number you want to analyze
# divisibility_results = analyze_number(anita)
#
# print(f"Analysis for {anita}:")
# for divisor, is_divisible in divisibility_results.items():
#     print(f"{anita} is divisible by {divisor}: {is_divisible}")

# =========================================================



# def analyze_number(anita):
#     basic_numbers = [2, 3, 5, 7, 11,13]  # You can add more basic numbers as needed
#
#     print(f"Analysis for {anita}:")
#
#     for divisor in basic_numbers:
#
#         is_divisible = anita % divisor == 0
#
#         print(f"{anita} is divisible by {divisor}: {is_divisible}")
#
# # Example usage
# anita = 30  # You can replace this with the number you want to analyze
# analyze_number(anita)



# ================================================================


def analyze_number(anita, basic_numbers):
    print(f"Analysis for {anita}:")

    for divisor in basic_numbers:
        is_divisible = anita % divisor == 0
        print(f"{anita} is divisible by {divisor}: {is_divisible}")


# Get user input for basic_numbers
user_input = input("Enter a comma-separated list of basic numbers: ")
basic_numbers = [int(num) for num in user_input.split(',')]

# Get user input for the number to analyze
anita = int(input("Enter the number to analyze: "))

# Perform analysis
analyze_number(anita, basic_numbers)
