def bubble_sort(scores, numbers):
    swapped = True

    while swapped:
        swapped = False         
        for i in range(0, len(scores)-1):
            if(scores[i] > scores[i+1] ):
                temp = scores[i+1]
                scores[i+1] =scores[i]
                scores[i] = temp

                temp = numbers[i+1]
                numbers[i+1] = numbers[i]
                numbers[i] = temp
                swapped = True  

score = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

number_of_scores = len(score)
solution_numbers = list(range(number_of_scores))    #list用法
print(solution_numbers)

bubble_sort(score, solution_numbers)
print("分数排序: ",score)
print("对应序号排序: ", solution_numbers)
