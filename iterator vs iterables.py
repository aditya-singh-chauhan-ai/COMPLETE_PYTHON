# Python example: iterable vs iterator
nums = [1, 2, 3]         # iterable
it = iter(nums)         # iterator
print(next(it))         # 1
print(next(it))         # 2
print(next(it))         # 3
# next(it) now raises StopIteration