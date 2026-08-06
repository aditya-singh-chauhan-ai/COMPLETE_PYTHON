# kwargs (keyword argument)
# ***kwargs (doube start)

# kwargs as a parameter
def func( **kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

# func('aditya', first_name = 'madhav', last_name = 'govind')

#dictionary unpacking
d= {'name' : 'aditya', 'age' : 24}
func(**d)