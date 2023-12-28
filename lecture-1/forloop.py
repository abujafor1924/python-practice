num = 17
for i in range(10, 0, -1):
    print(i)

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

number = [1, 5, 0, -4, 10, 9]
for val in number:
    if val < 0:
        break  # break is statement is stopped
    print(val)

i = 1
while i <= 10:
    if i == 7:
        i = i + 1  # Move the increment inside the if block
        continue # increase but if argument cross
    print(i)
    i = i + 1
