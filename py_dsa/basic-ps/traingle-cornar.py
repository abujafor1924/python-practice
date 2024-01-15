import math


def deg_to_radian(degree):
    return degree * math.pi / 180


def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def triangle():
    a, b, c = map(float, input("Enter Length of Three sides: ").split())

    # Convert angles to radians using deg_to_radian function
    angle_a = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
    angle_b = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    angle_c = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))

    angle_a = math.degrees(angle_a)
    angle_b = math.degrees(angle_b)
    angle_c = math.degrees(angle_c)

    print(f"Angles of the triangle are: {angle_a} degree, {angle_b} degree, {angle_c} degree")

    area = calculate_area(a, b, c)
    print(f"Area of the triangle is: {area}")


triangle()