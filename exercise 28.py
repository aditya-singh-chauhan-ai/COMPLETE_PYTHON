class Laptop:
    def __init__(self, brand, name, price):
        #instance variable
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand +' ' + name

    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name )
print(laptop1.apply_discount(90))