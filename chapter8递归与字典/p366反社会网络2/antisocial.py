names = ['Kim', 'John', 'Josh']
emails = ['kim@oreilly.com', 'john@abc.com', 'josh@wickedlysmart.com']

users = {'Kim' : 'kim@oreilly.com',
         'John' : 'john@abc.com',
         'Josh' : 'josh@wickedlysmart.com'}

for key in users:
    print(key ,':', users[key])

#
print("\n********************append User****************************")
users['Avary'] = 'avary@gmail.com'
for key in users:
    print(key ,':', users[key])

print("\n********************append User****************************")
del users['John']
for key in users:
    print(key ,':', users[key])

print("\n********************Judge****************************")
if 'Josh' in users:
    print("Josh's email address is:", users['Josh'])