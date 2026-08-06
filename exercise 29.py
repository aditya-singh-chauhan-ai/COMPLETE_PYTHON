class Person:
    count_instance = 0
    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        #instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = Person('Mahdva', 'Govind', 120)
p1 = Person('Mahdva', 'Govind', 120)
p1 = Person('Mahdva', 'Govind', 120)
print(Person.count_instance)
        