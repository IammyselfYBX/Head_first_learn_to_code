#for循环处理数字区间的方法
smoothies = ['coconut',
            'strawberry',
            'banana',
            'tropical',
            'acai berry']

length = len(smoothies) 
for i in range(length):
    print('Iterating through', i)
    print('Smoothie #', i, smoothies[i])