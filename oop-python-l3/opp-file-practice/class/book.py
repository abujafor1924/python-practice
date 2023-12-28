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
