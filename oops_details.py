# class Student:
#     college_name = 'abc'     #class attr    class.attr
#     def __init__(self, fullname, marks):
#         self.name = fullname    #instance attribute      obj.attr
#         self.marks = marks
#         print('adding new student in database...')

# s1 = Student('karan kumar', 97)
# print(s1.name, s1.marks, s1.college_name)
# s2 = Student('arjun kumar', 99)
# print(s2.name)
# # class Car:
# #     color = 'blue'
#     brand = 'bmw'
    
# car1 = Car()
# print(car1.color)
# print(car1.brand)

# #default constructor
#  def __init__(self):
#     pass

# #parameterized constructor
# def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
#         print('adding new student in database...')


# class Student:
#     college_name = 'abc'     
#     def __init__(self, fullname, marks):
#         self.name = fullname   
#         self.marks = marks

#     def welcome(self):
#         print('welcome Studens,', self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student('karan', 97)
# s1.welcome()
# print(s1.get_marks())




# class Students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod       #decorator   #static method
#     def hello():
#         print('hello')
    
#     def get_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum += i
#         print('hi', self.name, 'your avg score is:', sum/3)
# s1 = Students('adi', [99,98,97])
# s1.get_avg()

# s1.name = 'madhav'
# s1.get_avg()
# s1.hello()



# class Car:              #Abstraction
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print('car started...')

# car1 = Car()
# car1.start() 



class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self, amount):
        self.balance -= amount
        print('Rs.', amount, 'was debited')
        print('total balance =', self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print('Rs.', amount, 'was credited')
        print('total balance =', self.get_balance())

    #final balance
    def get_balance(self):
        return self.balance

    
    

acc1 = Account(10000, 12345)
acc1.debit(125)
acc1.credit(35)
acc1.debit(35626)
acc1.credit(200000)