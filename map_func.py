#map function

numbers = [1,2,3,4]

# def square(a):
#     return a**2

squares = list(map(lambda a :a**2, numbers))
print(squares)

#list compr
squares_new = [i**2 for i in numbers]
print(squares_new)