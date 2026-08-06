# RANDOM PASSWORD GENERATOR


import random
from shlex import join
import string

pass_len = 12
charVal = string.ascii_letters + string.digits + string.punctuation

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

password = "".join([random.choice(charVal) for i in range(pass_len )])
# password = ""
# for i in range(pass_len):
#     password += random.choice(charVal)

print('your password is:', password)



