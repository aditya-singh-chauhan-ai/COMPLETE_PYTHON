class Laptop:
    def __init__(self, brand, name, price):
        #instance variable
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand +' ' + name

laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name )