"""
Array practicing in python
comment is printed

"""
# random number
import random

print(random.randrange(1, 5))

a = """
Array practicing in python
"""
print(a)

# Assign multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# one value to multiple variable
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# string index
a = "Hello, World!"
print(a[1])  # e

# string length
a = "Hello, World!"
print(len(a))
# fer word count and showing
for x in "banana":
    print(x)

# text have line ? test it
txt = "The best things in life are free!"
print("free" in txt)

# text is present ?
txt = "The best things in life are free!"
if "life" in txt:
    print("Yes, 'best' is present.")

# show starting 2 then end 5
b = "Hello, World!"
print(b[2:5])  # llo

# upper string
a = "Hello, World!"
print(a.upper())

# lower string
a = "Hello, World!"
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The sp lit() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
