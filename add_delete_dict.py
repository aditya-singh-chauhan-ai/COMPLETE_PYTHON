user_info = {
    'name' : 'madhav',
    'age' : 20,
    'fav_movies' : ['govind', 'kri sh na'],
    'fav_tunes' : ['awake', 'fairy tale']

}

#add data
# user_info['fav_song'] = ['song1', 'song2']
# print(user_info)

#pop method
popped_item = user_info.pop('age')
# print(f"popped item is : {popped_item}")
print(type(popped_item))

#popitem method
# popped_item = user_info.popitem()
# print(type(popped_item))
# print(user_info)

