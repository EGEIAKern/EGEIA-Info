f = open('1.txt')
k=0
m = []
for s in f:
    a = sorted([int(x)for x in s.split()])
    k +=1
    a3 = [x for x in a if a.count(x)== 3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 3 and len(a1) == 4 and (a1[0] + a1[1]+a1[2]+a1[3])/4 > (a3[0] + a3[1] + a3[2])/3:
        m.append(k)
print(m[-1])
