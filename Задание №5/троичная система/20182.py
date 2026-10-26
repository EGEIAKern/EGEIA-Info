def C3(x):
    s = ''
    while x > 0:
        s = str(s%3) +s
        x = x //3
for n in range(1,1000):
    b = C3(n)
    k1 = b.count('1')
    if k1%2==0:
        b = b +'0'
        b = '12' + b[2:]
    else:

