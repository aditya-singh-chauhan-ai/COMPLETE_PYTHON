x = 5 #global variable
def func():
    global x
    x = 7 #local variable
    return x

# def func2():
#     print(x)  # This will raise a NameError since x is not defined in this scope

# func2()

print(x)  # This will print 5
print(func())  # This will print 7
print(x)  # This will raise a NameError since x is not defined in this scope