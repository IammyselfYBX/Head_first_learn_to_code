my_file = open('lib.txt', 'r')

while True:
    line = my_file.readline()
    if line != '':  # 文章结尾会是一个空串
        print(line)
    else:
        break

my_file.close()