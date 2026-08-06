# all any function

numbers1 = [2,4,6,8,10]
numbers2 = [1,3,6,7,9]

print(all([num%2==0 for num in numbers1]))
print(all([num%2==0 for num in numbers2]))
print(any([num%2==0 for num in numbers2]))
