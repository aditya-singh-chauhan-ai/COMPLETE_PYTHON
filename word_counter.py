#word counter
# d = {'a' : 3, 'd' : 2, 'a' : 5 }
# print(d)

def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

print(word_counter('madhav'))