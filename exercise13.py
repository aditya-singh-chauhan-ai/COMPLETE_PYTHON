
# def is_palindrome(word):
#     reverse_word = word[::-1]
#     if word == reverse_word:
#         return True
#     else:
#         return False

# print(is_palindrome("naman"))
# print(is_palindrome("python"))


# def is_palindrome(word):
#     if word == word[: : -1]:
#         return True
#     return False
# print(is_palindrome("naman"))
# print(is_palindrome("python"))

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("naman"))
print(is_palindrome("python"))