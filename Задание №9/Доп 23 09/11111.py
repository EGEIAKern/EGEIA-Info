f = open('11111.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    if len(set(a)) == 5 and 2*(a[0]+a[-1]) > a[1] + a[2] + a[3]:
        print(sum(a))
        break