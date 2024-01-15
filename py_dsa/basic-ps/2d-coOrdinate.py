import math

x1, y1 = map(float, input("Enter Coordinates of First point (x1 y1): ").split())
x2, y2 = map(float, input("Enter Coordinates of Second point (x2 y2): ").split())

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The distance is:", distance)
