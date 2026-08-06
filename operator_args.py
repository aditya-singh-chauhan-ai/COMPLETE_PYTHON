# *operator
# *args


# def all_total(*args):
#     print(args)
#     print(type(args))

# all_total(1,2,3,4,5,65)

def all_total(*args):
    total = 0
    for num in args:
        total+= num
    return total
print(all_total(1,2,3,4,5,65))