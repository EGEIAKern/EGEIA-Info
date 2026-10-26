f = open('31355.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a3 = [x for x in a if a.count(x)==3] # 3 повторяются
    a1 = [x for x in a if a.count(x) == 1] #повторяется 1 раз
    if len(a3) == 3 and len(a1) == 3 and a3[0] ** 3 < a1[0] * a1[1] * a1[2]:
        k+=1
print(k)