class Dog:
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.leg = 4

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.name, self.color, "is", self.leg, "leg dog smiling")


d1 = Dog("robat", "Brown")
d2 = Dog("hati", "Whit")

d1.poke()
d1.update_color("Black")
d1.poke()
d2.poke()

print(d1.__dict__)  # dictionary formate
print(dir(d1))  # direction method
