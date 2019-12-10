marbles = [10, 13, 39, 14, 41, 9, 3] 

#方法1:使用python内置函数 sum()
print('Python sum(): The total is', sum(marbles))

#方法2:求和函数
def computer_sum(list):
    sum = 0

    for number in list:
        sum += number
    
    return sum

print("Sum function: The total is", computer_sum(marbles))
        

#方法3:递归方法
def recursive_compute_sum(list):
    if len(list) == 0:
        return 0
    else:
        first = list[0]
        rest = list[1:]
        sum = first + recursive_compute_sum(rest)
        return sum

sum = recursive_compute_sum(marbles)
print('recursive: The total is', sum)