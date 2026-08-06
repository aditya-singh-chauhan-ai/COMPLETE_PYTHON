# #dictionaries intro
# #why we use?
# # because of limitations of lists, lists are not enough to represents real data

# #example
# user = ['madhav', 20, ['govind', 'kri sh na'], ['awake', 'fairy tale']]
# #this list contains user name, age, fav mov, fav tune

# #unordered collections of data in keu : value pair.

# user = {'name' : 'madhav', 'age' : 20}
# # print(user)
# # print(type(user))

# #second method
# user1 = dict(name = 'madhav', age = 20)
# print(user1)

# #how to access data from dict
# print(user['name'])

# #which type of data a dict can store- anything

user_info = {
    'name' : 'madhav',
    'age' : 20,
    'fav_movies' : ['govind', 'kri sh na'],
    'fav_tunes' : ['awake', 'fairy tale']

}
# print(user_info['fav_movies'])

#how to add data to empty dict

user_info2 = {}
user_info2['name'] = 'madhav'
print(user_info2)