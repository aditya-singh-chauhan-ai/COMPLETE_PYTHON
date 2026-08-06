from turtle import circle


class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2*Circle.pi*self.radius
    
c = Circle(4)
c1 = Circle(6)
print(c.circumference())

class Laptop:
    discount_percent = 10
    def __init__(self, brand, name, price):
        #instance variable
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand +' ' + name

    def apply_discount(self):
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price

laptop1 = Laptop('hp', 'au114tx', 63000)
print(laptop1.laptop_name )
# print(laptop1.apply_discount(90)
laptop1.discount_percent = 50
print(laptop1.apply_discount())