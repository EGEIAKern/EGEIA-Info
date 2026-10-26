f = open('3.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a3 = [x for x in a if a.count(x) == 3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 6 and len(a1) == 1 and a3[-1] > a1[0]:
        k+=1
print(k)