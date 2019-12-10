harry = {'firstname' : 'Harry',
         'lastname' : 'Potter',
         'house' : 'Gryffindor',
         'friend' : ['Ron', 'Hermione'],
         'born' : '1980'}

print(harry)
for key in harry:
    print(key, ':', harry[key])