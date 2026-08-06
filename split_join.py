#split - converts a string into a list based on a delimiter
#join - converts a list into a string based on a delimiter
# user_info = "John,Doe,30,New York".split(",")
# print(user_info)  # Output: ['John', 'Doe', '30', 'New York']
# name, age = input("Enter your name and age separated by a comma: ").split(",")
# print(f"Name: {name}, Age: {age}")

#join example
user_info = ["Jane", "Doe", "25", "Los Angeles"]
print(",".join(user_info))  # Output: Jane,Doe,25,Los Angeles