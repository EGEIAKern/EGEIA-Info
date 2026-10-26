f = open('6.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a2 = [x for x in a if a.count(x)==2]
    a1 = [x for x in a if a.count(x)== 1]
    if len(a2) == 2 and len(a1) == 2 and a[-1] < a[1] + a[2] + a[0]:
        k += 1
print(k)