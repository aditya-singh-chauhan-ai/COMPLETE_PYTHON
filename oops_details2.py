# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student('aditya')
# del s1.name
# print(s1)

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account('12354', 'abcde')
# print(acc1.acc_no)
# print(acc1.reset_pass())


# class Person:
#     __name = 'ani'

#     def __hello(self):
#         print('hello')

# p1 = Person()

# print(p1.__hello)


# from turtle import color


# class Car:
#     color = 'black'
#     @staticmethod
#     def start():
#         print('car start')

#     @staticmethod
#     def stop():
#         print('car stop')

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar('fortune')
# car2 = ToyotaCar('innova')
# print(car1.start())
# print(car1.stop())
# print(car2.color)


# class A:
#     varA = 'wel to class A'

# class B:
#     varB = 'wel to class B'

# class C(A, B):
#     varC = 'wel to class C'

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)
# print(C())



# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print('car start')

#     @staticmethod
#     def stop():
#         print('car stop')

# class ToyotaCar(Car):
#     def __init__(self, name, type='gas'):
#         # accept a type parameter (default to 'gas') and pass it to the base class
#         super().__init__(type)
#         self.name = name
        

# car1 = ToyotaCar('fortune', 'electric')
# car2 = ToyotaCar('innova')

# # call start/stop directly (they print messages) instead of printing their return value (None)
# car1.start()
# car1.stop()

# print(car1.type)



# class Person:
#     name = 'anon'

#     # def changeName(self, name):
#     #     self.__class__.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName('adiii')
# print(p1.name)
# print(Person.name)

# from time import perf_counter


# class Student:
#     def __init__(self, phy, che, math):
#         self.che = che
#         self.phy = phy
#         self.math = math

#     # def calcpercentage(self):
#     #     self.percentage = str((self.phy + self.che + self.math) / 3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy + self.che + self.math) / 3) + "%"
    
# s1 = Student(98,95,96)
# print(s1.percentage)

# s1.phy = 50
# # s1.calcpercentage()
# print(s1.percentage)

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNum(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(1,3)
# num1.showNum()

# num2 = Complex(5,9)
# num2.showNum() 

# num3 = num1 - num2
# num3.showNum()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def parameter(self):
#         return 2 * 3.14 * self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.parameter())
# print(c1.radius)


# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showData(self):
#         print('role =', self.role)
#         print('dept =', self.dept)
#         print('salary =', self.salary)

# class Engineer(Employee):
#         def __init__(self, name, age):
#             self.name = name
#             self.age = age
#             super().__init__('Engineer', 'IT', '900000')

# engg1 = Engineer('elon', 40)
# engg1.showData()

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order('chips', '30')
ord2 = Order('kur', '55')
print(ord1 > ord2)     #True