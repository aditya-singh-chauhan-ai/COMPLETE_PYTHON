string= "madhav"
print(string[1])
# string[1] = 'A'  # This will raise an error because strings are immutable
print(string.replace("a", "A",2))  # This will create a new string, original remains unchanged
# print(string)  # Output: madhav