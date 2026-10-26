for n in range(2,1000):
    b = [int(d) for d in str(n)]
    s1 = sum(d for d in b if d%2==0)
    s2 = 0
    for i in range(len(b)):
        if(i+1)%2==0:
            s2 = s2 +b[i]
    r = abs(s2-s1)
    if r == 7:
        print(n,r)

