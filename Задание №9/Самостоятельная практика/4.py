f = open('4.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    an = [x for x in a if a.count(x)>1]
    amax = [x for x in a if a.count(x) == 1 and x == a[-1]]
    a = [x for x in a if a.count(x) == 1]
    if len(an) > 1 and len(amax) == 1 and sum(an) > sum(a):
        k +=1
print(k)
