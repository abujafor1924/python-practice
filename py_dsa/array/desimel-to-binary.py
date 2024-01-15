decimal_number = int(input("Enter Your Number : "))
binary_representation = bin(decimal_number)

print(f"The binary of {decimal_number} is: {binary_representation}")



# def decimal_to_binary(decimal):
#     if decimal == 0:
#         print("Binary represent: 0")
#         return
#
#     binary_array = []
#     index = 0
#
#     while decimal > 0:
#         binary_array.append(decimal % 2)
#         decimal //= 2
#
#     print("Binary representing:", end=" ")
#
#     for i in range(len(binary_array) - 1, -1, -1):
#         print(binary_array[i], end="")
#
#     print()
#
#
# def main():
#     n = int(input("Enter Your Decimal Number: "))
#     decimal_to_binary(n)
#
#
# if __name__ == "__main__":
#     main()
