#增加更多的属性
"""
email = {'Kim' : 'kim@oreilly.com',
         'John' : 'john@abc.com',
         'Josh' : 'josh@wickedlysmart.com'}

genders = {'Kim' : 'f',
           'John' : 'm',
           'Josh' : 'm'}
"""

# 不要使用上面的结构,因为这样又回到管理两个结构的老路,很麻烦,采取下面的结构
attributes = {
            'email' : 'kim@oreilly.com',
            'genders' : 'f',
            'age' : 27,
            'friends' : ['John', 'Josh']
            }

users = {}
users['Kim'] = attributes
users['John'] = {
                'email' : 'john@abc.com',
                'genders' : 'm',
                'age' : 24,
                'friends' : ['Kim', 'Josh']
                }

users['Josh'] = {
                'email' : 'josh@wickedlysmart.com',
                'genders' : 'm',
                'age' : 32,
                'friends' : ['Kim']
                }
print(users)

print("\n*****************for*********************")
for key in users:
    print(key, ':', users[key])