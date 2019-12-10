my_dictionary = {}

my_dictionary['jenny'] = '867-5309'
my_dictionary['paul'] = '555-1201'
my_dictionary['jamie'] = '771-0091'
my_dictionary['paul'] = '443-0000'

print("Jenny's number is", my_dictionary['jenny'])
print('length of the my_dictionary', len(my_dictionary))

if 'jenny' in my_dictionary:
    del(my_dictionary['jenny'])
else:
    print('I need to get her number')

print('length of the my_dictionary', len(my_dictionary))