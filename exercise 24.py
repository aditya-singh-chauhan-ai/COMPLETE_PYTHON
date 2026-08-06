def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return 'you didnt pass ay args'

nums = [1,2,3]

print(to_power(3, *[2,3]))