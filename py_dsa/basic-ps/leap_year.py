year = int(input("Enter Your leap Year: "))
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

    print(f"{year} is a Leap Year ")
else:
    print(f"{year} is not a Leap Year ")
