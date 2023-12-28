class Student:
    def __init__(self, name, Id):
        self.Id = Id  # instance Variable
        self.name = name  # instance Variable
        # print("a Student added this List")

    def details(self):  # instance Method
        print("Name:", self.name, "ID:", self.Id)


# variable = class_Name()
s1 = Student("joni", 11)
s2 = Student("Rahat", 34)
s1.Id = 22  # Change s1 Value
s1.details()
s2.details()

# print("s1", s1)  # address
# print("s2", s2)  # address
# print(s1.name)
# print(s1.Id)
# s1.Id = 23  # Change Value
# print(s1.Id)
# print(s2.name)
# print(s2.Id)
