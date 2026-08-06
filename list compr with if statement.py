#list compr with if statement

num = list(range(1,11))
# nums = []
# for i in num:
#     if i%2 == 0:
#         nums.append(i)
# print(nums)

even = [i for i in num if i%2 == 0]
odd = [i for i in num if i%2 != 0]
print(even)
print(odd)