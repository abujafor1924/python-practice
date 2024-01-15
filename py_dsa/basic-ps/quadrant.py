# Get user input for coordinates
# x = float(input("Enter the x-coordinate: "))
# y = float(input("Enter the y-coordinate: "))
#
# # Determine the quadrant
# if x > 0 and y > 0:
#     print("The point is in the first quadrant.")
# elif x < 0 and y > 0:
#     print("The point is in the second quadrant.")
# elif x < 0 and y < 0:
#     print("The point is in the third quadrant.")
# elif x > 0 and y < 0:
#     print("The point is in the fourth quadrant.")
# elif x == 0 and y == 0:
#     print("The point is at the origin.")
# elif x == 0:
#     print("The point is on the y-axis.")
# elif y == 0:
#     print("The point is on the x-axis.")



# =========================================================
x, y = map(float, input("Enter the coordinates (x y): ").split())

if x == 0 and y == 0:
    print("The point is at the origin.")
elif x == 0:
    print("The point is on the y-axis.")
elif y == 0:
    print("The point is on the x-axis.")
else:
    quadrant = 1 if x > 0 and y > 0 else 2 if x < 0 and y > 0 else 3 if x < 0 and y < 0 else 4
    print(f"The point is in the {quadrant} quadrant.")
