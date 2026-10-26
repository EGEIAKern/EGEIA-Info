for n in range(2,100000):
    x = n
    if x%3==0:
        x = x//3
    else:
        x = x - 1
    if x%7==0:
        x = x// 7
    else:
        x = x - 1
    if x %11==0:
        x = x // 11
    else:
        x = x - 1
    if x == 6:
        print(n,x)