# def func(item):
#     return  len(item)

# names = ['madhav', 'govinda', 'krishnaa']
# print(min(names, key = lambda item : len(item)))

students = {
    'aditya' : {'score' : 90, 'age' : 20},
    'madhav' : {'score' : 99, 'age' : 120},
    'govind' : {'score' : 100, 'age' : 120}
}

print(max(students, key = lambda item:students[item]['age']))

students2 = [
    {'name' : 'aditya', 'score' : 90, 'age' : 20},
    {'name' : 'madhav','score' : 99, 'age' : 120},
    {'name' : 'govind','score' : 100, 'age' : 120}
]
print(max(students2, key = lambda item:item.get('score'))['name'])