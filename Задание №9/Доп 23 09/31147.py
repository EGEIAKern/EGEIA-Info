f = open('31147.txt')
m =[]
k=0
for s in f:
    a = sorted([int(x)for x in s.split()])
    k+=1 #добавляем номер строки к каждому списку
    if len(set(a)) == 6 and 2*(a[0]+a[1]+a[2] < a[3]+a[4]+a[5]):
        m.append(k)
print(m[-1])
