def reverse_elements(l):
    elements = []
    for i in l:
        elements.append(i[::-1])
    return elements

words = ['hello', 'world', 'python', 'rocks']
print(reverse_elements(words))
