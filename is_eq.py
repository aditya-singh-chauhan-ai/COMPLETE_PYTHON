fruits1 = ['apple', 'banana', 'cherry']
fruits2 = ['apple', 'banana', 'cherry']
fruits3 = ['apple', 'banana', 'date']
print(fruits1 == fruits2)  # True, as both lists have the same elements in the same order
print(fruits1 == fruits3)  # False, as the lists differ in the last element
print(fruits1 is fruits2)  # False, as they are different objects in memory
print(fruits1 is fruits1)  # True, as both refer to the same object in memory
