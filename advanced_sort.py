# fruits = ('graphes', 'mango', 'apple')
# print(sorted(fruits))

guitars = [
    {'model' : 'yamaha f310', 'price' : 84000},
    {'model' : 'faith naptune', 'price' : 5000},
    {'model': 'taylor', 'price' : 450000} 
]

# print(sorted(guitars, key = lambda d:d['price']))

print(sorted(guitars, key=lambda d: d['price'], reverse = True))