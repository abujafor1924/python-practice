class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def detail(self):
        print("Book Name:", self.name,
              "\nAuthor", self.author,
              "\nPrice", self.price, "Taka")

# design Classes


# =================================================

# b1 = Book("onila sundory", "Humaun ahmed")
# b1.detail()
# b1.set_price(220)
# print(b1.get_price())
# b1.detail()
