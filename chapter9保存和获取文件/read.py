my_file = open('/home/tony/Downloads/Head_first_learn_to_code/chapter9保存和获取文件/lib.txt', 'r')

my_text = my_file.read()
print(my_text)
my_file.close()