"""

Basic topic practice
** Function Recursion

"""


# Function Recursion
def recurs(n):
    if n == 1:
        return 1
    else:
        return n * recurs(n - 1)  # self return function


print(recurs(5))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(5, 6))

z = lambda a, b, c: a + b + c
print(z(2, 3, 4))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
