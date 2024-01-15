def calculet_traingle_area(vertices):
    x1, y1, x2, y2, x3, y3 = vertices
    area = .5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area


vertices = [float(input(f"Enter Your coordinate vertices {i + 1} :")) for i in range(6)]

trn = calculet_traingle_area(vertices)
print("Area of triangle = ", trn)
