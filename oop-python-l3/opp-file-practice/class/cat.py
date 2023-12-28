class Cat:
    def __init__(self, color, action):
        self.color = color
        self.action = action

    def view(self, num, clr):
        num = num + 5
        clr[1] = "Green"
        print("Method Inside", num)
        print("Method Inside", clr)
        # print(self.color, "Cat is ", self.action)

    # def compare(self, ct):
    #     if self.action == ct.action:
    #         print("Both cat are ", self.action)
    #     else:
    #         print("They are difference")


# ====================================
colors = ["black", "orange", "white", "yellow"]
c1 = Cat("red", "Laughing")
# c2 = Cat("Black", "crannying")
x = 55
c1.view(x, colors)
print("Method Outside", x)
print("Method Outside", colors)
# c1.view()
# c2.view()
# c1.compare(c2)
