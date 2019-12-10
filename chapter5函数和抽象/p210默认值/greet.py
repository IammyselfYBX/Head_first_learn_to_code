#这是一个建议,需要设置默认值,因为有可能很多用户疏忽导致系统的出错

def greet(name, message='You rule!'):
    print('Hi',name + '.',message)

greet("john")
greet("YBX","is the most handsome man in NCEPU")