import inspect

class Electronic_Gadgets:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year_of_invent = year

class Pocket_Gadgets(Electronic_Gadgets):
    def __init__(self, size):
        self.size = size

class Phones(Pocket_Gadgets):
    def __init__(self, ram, camera):
        self.ram = ram
        self.camera = camera

    def printdetails(self):
        return f"Name : {self.name}\nPrice : {self.price}\nRAM : {self.ram}"

samsung = Phones(6, 64)
samsung.name = "Samsung S7 Edge"
samsung.price = 25000
samsung.year_of_invent = 2020
print(samsung.printdetails())