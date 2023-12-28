a = 10
b = 20

a = a + b  # The value of 'a' becomes 30 (10 + 20)
b = a - b  # The value of 'b' becomes -10 (20 - 30)
a = a - b  # The value of 'a' becomes -40 (-10 - 30)

# print(a)
# print(b)


num = int(input("Enter Your Number : "))

if num >= 0:
    if num == 0:
        print("Zero Number")
    else:
        print("Positive Number")

else:
    print("Negative Number")
