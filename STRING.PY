first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)
# print(full_name + 3)  # This will raise a TypeError
print(full_name + str(3))  # This will work
print(full_name * 3)  # This will repeat the string 3 times
print(" ".join([full_name] * 3))  # This will repeat the string 3 times with spaces