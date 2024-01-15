import math


def calculate_circumference(radius):
    if radius < 0:
        return "Radius cannot be negative."

    circumference = 2 * math.pi * radius
    return circumference


# Example usage
radius = float(input("Enter the radius of the circle: "))
perimeter = calculate_circumference(radius)

if type(perimeter) == str:
    print(perimeter)
else:
    print(f"The circle with radius {radius} is {perimeter:.2f}.")
