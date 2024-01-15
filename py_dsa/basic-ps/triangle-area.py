import math


def calculate_area(sid1, sid2, sid3):
    s = (sid1 + sid2 + sid3) / 2
    area = math.sqrt(s * (s - sid1) * (s - sid2) * (s - sid3))
    return area


def main():
    sid1 = float(input("Enter First sid: "))
    sid2 = float(input("Enter second sid: "))
    sid3 = float(input("Enter Third sid: "))

    if sid1 + sid2 > sid3 and sid1 + sid3 > sid2 and sid2 + sid3 > sid1:
        area = calculate_area(sid1, sid2, sid3)
        print("The area of the triangle is:", area)
    else:
        print("Invalid input. The given sides do not form a valid triangle.")


if __name__ == "__main__":
    main()
