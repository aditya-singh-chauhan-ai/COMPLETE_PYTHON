#filter function
# import numbers
# def is_even(a):
#     return a%2==0

numbers = [3,4,56,9,87,6,2]

evens = tuple(filter(lambda a:a%2==0, numbers))
# print(evens)

for i in evens:
    print(i)

for i in evens:
    print(i)