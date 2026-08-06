class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_spec = f"{self.brand} {self.model_name} and price is {self._price}"
    
    
    def make_a_call(self, phone_number):
        print(f"calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"
    
    @property
    def complete_spec(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price, 0)
        
phone1 = Phone('nokia', '1100', 1000)
print(phone1.brand)
print(phone1.model_name)
phone1._price = 500
print(phone1._price)
print(phone1.complete_spec)