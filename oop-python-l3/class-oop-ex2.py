class House:
    def __init__(self):
        self.window = 4
        self.door = 2

    def vew(self):
        print(self.window, "Window", self.door, "Door")


h1 = House()
h2 = House()
print(h1)
print(h2)
h1.window = 8
h2.door = 3
h1.vew()
h2.vew()
