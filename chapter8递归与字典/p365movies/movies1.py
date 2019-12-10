movies = [] #列表
movie = {}  #字典

# 使用两种方式创建字典
movie['name'] = 'Forbidden Planet'
movie['year'] = 1957
movie['rating'] = '*****'
movie['year'] = 1956

# 将字典追加到列表里面
movies.append(movie)

movie2 = {'name': 'I Was a Teenage Werewolf',
               'year': 1957, 'rating': '****'}
movie2['rating'] = '***'

movies.append(movie2)

movies.append({'name': 'Viking Women and the Sea Serpent',
               'year': 1957,
               'rating': '**'})

movies.append({'name': 'Vertigo',
               'year': 1958,
               'rating': '*****'})

print('Head First Movie Recommendations')
print('--------------------------------')
for movie in movies:
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')',  movie['year'])
