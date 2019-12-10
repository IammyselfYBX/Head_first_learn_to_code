def bubble_sort(scores):
    swapped = True

    while swapped:
        swapped = False         #这一步很关键
        for i in range(0, len(scores)-1):
            if(scores[i] > scores[i+1] ):
                temp = scores[i+1]
                scores[i+1] =scores[i]
                scores[i] = temp
                swapped = True  #这一步很关键

score = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

bubble_sort(score)
print(score)

smoothies = ["cocount", "strawberry", "Banana", "Pineapple"]    #如果不统一大小写的话,根据ASCII码表比较
bubble_sort(smoothies)
print(smoothies)

smoothies = ["Cocount", "strawberry", "Banana", "Pineapple"]    #如果不统一大小写的话,根据ASCII码表比较
bubble_sort(smoothies)
print(smoothies)