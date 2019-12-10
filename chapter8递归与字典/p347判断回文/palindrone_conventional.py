# 本函数功能是使用while循环判断回文的方法

def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            print(word, "这不是回文")
            return False
        i = i + 1
        j = j - 1
        
    print(word, "这是回文")
    return True

print(is_palindrome('radar'))
print(is_palindrome('raddar'))
print(is_palindrome('ruddar'))

