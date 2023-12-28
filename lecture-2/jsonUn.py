
import json


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# Load the JSON string into a Python object:
data = json.loads(y)


# Access the "cars" key to retrieve the list of cars:
car_list = data["cars"]


# the result is a JSON string:
print(car_list[0]["model"])


# Python String Formatting
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

price = 49
txt = "The price is {:.4f} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

