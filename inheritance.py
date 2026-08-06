# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)

#     def make_a_call(self, number):
#         return f"calling {number} ..."

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
    
# class SmartPhone(Phone):
#     def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
#         #two ways
#         Phone.__init__(self, brand,model_name,price)
#         self.ram = ram
#         self.internal_memory = internal_memory
#         self.rear_camera = rear_camera


# phone1 = Phone('nokia', '1100', 1000)
# print(Phone.full_name())
# phone2 = SmartPhone('nokia', '1100', 1000, '6 gb', '64 gb', '20 mp')
# print(SmartPhone.full_name())


# ...existing code...
class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, number):
        return f"calling {number} ..."

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

# create instances
phone1 = Phone('nokia', '1100', 1000)
print(phone1.full_name())              # call on instance

phone2 = SmartPhone('samsung', 'galaxy', 1000, '6 gb', '64 gb', '20 mp')
print(phone2.full_name())              # call on smartphone instance
# ...existing code...