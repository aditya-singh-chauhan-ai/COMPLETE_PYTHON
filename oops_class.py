class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        return cls(first, last, int(age))

    @classmethod
    def count_instances(cls):
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# create instances
p1 = Person('Mahdva', 'Govind', 120)
p2 = Person.from_string('Mahdva,Govind,120')
p3 = Person('Mahdva', 'Govind', 120)

print(Person.count_instances())  # call the method with ()
print(p2.full_name())





# class Person:
#     count_instance = 0

#     def __init__(self, first_name, last_name, age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     @classmethod
#     def from_string(cls, string):
#         first, last, age = string.split(",")
#         return cls(first, last, int(age))

#     @classmethod
#     def count_instances(cls):
#         return f"you have created {cls.count_instance} instances of {cls.__name__} class"

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

# # create instances
# p1 = Person('Mahdva', 'Govind', 120)
# p2 = Person.from_string('Mahdva,Govind,120')
# p3 = Person('Mahdva', 'Govind', 120)

# print(Person.count_instances())  # call the method with ()
# print(p2.full_name())
        