f = open('31217.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a1 = [x for x in a if a.count(x) == 2]
    a2 = [x for x in a if a.count(x) == 1]
    if len(a1) == 4 and len(a2) == 2 and sum(a1) > sum(a2):
        k+=1
print(k)