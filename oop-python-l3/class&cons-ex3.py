class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.wheel = 4

    def details(self):
        print("This is Car of ", self.name, " is", self.model)
        print("It is a ", self.wheel, "Wheel Car")


c1 = Car("BMW", 2015)
c2 = Car("Aodi", 2018)
c1.details()
c2.details()
