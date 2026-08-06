#in keyword and iterations in dicionary

user_info = {
    'name' : 'madhav',
    'age' : 20,
    'fav_movies' : ['govind', 'kri sh na'],
    'fav_tunes' : ['awake', 'fairy tale']

}

# #check if key exist in dict
# if 'names' in user_info:
#     print('present')
# else:
#     print('not')

# #check if value exist     .values method
# if 'madhav' in user_info.values():
#     print('present')
# else:
#     print('not')

#loops in dict
# for i in user_info.values():
#     print(i)

#values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

#keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

#items method ------------- most useful method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

# for key, value in user_info.items():
#     print(f"key is {key} and value is {value}")

for i in user_info.items():
    # print(f"key is {key} and value is {value}")
    print(i)