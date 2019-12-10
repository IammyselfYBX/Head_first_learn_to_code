cup1 = 0
cup2 = 1
cup3 = 0
#0 1 0

cup1 = cup1 + 1
cup2 = cup1 - 1
cup3 = cup1
#1 0 1

cup1 = cup1 * 0
cup2 = cup3
cup3 = cup1
#0 1 0

cup1 = cup2 % 1
cup3 = cup2
cup2 = cup3 - cup3
#0 0 1

print(cup1)
print(cup2)
print(cup3)