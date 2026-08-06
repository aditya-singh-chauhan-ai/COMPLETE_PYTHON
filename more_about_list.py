#generate lists with range functions
#something more about pop method
#index method
#pass list to a function

# numbers = list(range(1, 22))
# print(numbers)
# print(numbers.pop())
# print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(numbers.index(1))
# print(numbers.index(1, 2))  # start searching from index 2

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))