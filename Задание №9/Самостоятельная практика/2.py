f = open('2.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    amax = [x for x in a if x == a[-1] and a.count(x) == 2]
    a1 = [x for x in a if a.count(x)==1]
    if len(amax) == 2 and len(a1) == 5 and a1[-1]**2 + a1[0] ** 2 > (a1[1] + a1[2]+a1[3])**2:
        k +=1
print(k)