# f = open('demo.txt')
# line1 = f.readline()
# print(line1)
# # print(type(data))
# line2 = f.readline()
# print(line2)

# f.close() 
# f = open('sample.txt', 'w')
# f.write("\n i think it was easy")


# f.close()

# f = open('sample.txt', 'r+')          #no trunctae
# f.write('abc')
# print(f.read())
# f.close()

# f = open('sample.txt', 'w+')              # truncate
# # f.write('abc')
# print(f.read())
# f.write('abcddd')
# f.close()

# f = open('sample.txt', 'a+')                #no trunc
# # f.write('abc')
# print(f.read())
# f.write('12')
# f.close()

# with open('demo.txt','r') as f:
#     data = f.read()
#     print(data)

# with open('demo.txt','w') as f:
#     f.write('hiiiiiiii')


# deleting a file

# import os
# from random import sample
# os.remove('sample.txt')


# with open('practice.txt', 'r') as f:
#     data = f.read()

# new_data = data.replace('java', 'python')
# print(new_data)
#     # f.write("Hi everyone\nwe are learning file handling\nusing java.\ni like programming in java")


# with open('practice.txt', 'w') as f:
#     f.write(new_data)


# def check_for_word():
#     word = "learning"
#     with open('practice.txt', 'r') as f:
#         data = f.read()
#     if (data.find(word)):
#         print('found')
#     else:
#         print('not foound')

# def check_for_line():
#     word = 'pyqq'
#     data = True
#     line_no = 1
#     with open('practice.txt') as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1
# print(check_for_line())

from itertools import count


count = 0
with open('practice.txt') as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]


nums = data.split(",")
for val in nums:
    if(int(val) % 2 ==0):
        count += 1

print(count)