user = {}

name = input('what is your name :')
age = input('what is your age :')
fav_movies = input('your fav movies separated by comma  ').split(',')
fav_song = input('your fav song separated by comma  ').split(',')

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song

for key, value in user.items():
    print(f"{key} : {value} ")


