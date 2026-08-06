string = "madhav"
first_index = string.find('a')
second_index = string.find('a', first_index + 1)
if second_index != -1:
    string = string[:second_index] + 'A' + string[second_index + 1:]
print(string)  # Output: madhAv
