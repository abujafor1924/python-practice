def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return original_number == reversed_number


def palindrom_area():
    n = int(input("Enter your targeted Number: "))

    for i in range(n):
        if is_palindrome(i):
            print(i, end=" \t")


palindrom_area()
