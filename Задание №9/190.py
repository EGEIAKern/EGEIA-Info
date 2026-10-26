# 6 чисел. Определить строки, для которых выполнено ровно одно из двух условий
# 1. В строке есть повторяющиеся числа
# 2. В строке есть 3 нечётных числа
f = open('190.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a3 = [x for x in a if a.count(x) > 1]
    a1 = [x for x in a if x%2 != 0]
    if (len(a3) > 1) + (len(a1) == 3)==1:
        k +=1
print(k)