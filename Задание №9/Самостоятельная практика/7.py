f = open('7.txt')
for s in f:
    a = sorted([int(x)for x in s.split()])
    if a[0] < a[1] < a[2] < a[3] < a[4] < a[5] < a[6] and (a[0] + a[-1])/2 > (a[1] + a[2] +a[3] + a[4]+ a[5])/5:
        print(sum(a))
        break

