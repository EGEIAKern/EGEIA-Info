#кол-во строк, в которых числа можно разбить на 3 пары, состоящих из одинаковых чисел
f = open('157.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    if a[0] == a[1] and a[2]==a[3] and a[4] == a[5]:
        k +=1
print(k)