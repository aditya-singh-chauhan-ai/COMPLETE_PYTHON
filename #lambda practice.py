#lambda practice

iseven = lambda a : a%2==0
print(iseven(6))

last_char = lambda s : s[-1]
print(last_char('madhav'))

# lambda with if else

func = lambda s : True if len(s) > 5 else False
print(func('madhav'))