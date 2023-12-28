print("What operation do you what?")
operator = input("Enter Operator + , - , / , * : ")
n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))

if operator == '+':
    print(n1, operator, n2, "=", n1 + n2)
elif operator == '-':
    print(n1, operator, n2, "=", n1 - n2)
elif operator == '*':
    print(n1, operator, n2, "=", n1 * n2)
elif operator == '/':
    print(n1, operator, n2, "=", n1 / n2)
else:
    print("Invalid Operation")
