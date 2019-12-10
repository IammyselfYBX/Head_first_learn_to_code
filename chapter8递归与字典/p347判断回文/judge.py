# 本函数功能是使用循环判断回文的方法
 
string = "tacocat"
string1 = "abcd"

def judge(test):
    length = len(test)
    for i in range(length):
        if test[i] == test[length-1 - i]:
            continue
        else:
            print(test, "这不是回文")
            return 1

    print(test, "这是回文")

judge(string)
judge(string1)