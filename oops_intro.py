#what is class
#how to create an class
#what is init method
#what are attributes instances variables
#how to create our object


class Person:
    def __init__(self, first_name, last_name, age):
        print('init method called')
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    

p1 = Person('madhav', 'govind', 25)

print(p1.first_name)