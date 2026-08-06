#in keyword in sets and for loop

# s = {'a', 'b', 'c', 'd'}

# # in keyword to check if item is present or not in set
# if 'a' in s:
#     print("present")
# else:
#     print('not')

# #for loop
# for item in s:
#     print(item)

s1 = {1,2,3,4}
s2 = {3,4,5,6}


#union --------- use |

union_set = s1 | s2
print(union_set)


#intersection --------- use &
inter_set = s1 & s2
print(inter_set)
