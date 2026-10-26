m = []
def C3(x):
    s = ''
    while x>0:
        s = str(x%3) +s
        x = x//3
    return s
for n in range(1,1000):
    b = C3(n)
    k1 = b.count('1')
    k2 = b.count('2')
    k = k1+k2*2
    if k%3==0:
        b = '112' + b[2:]
    else:
        b = b + C3(k)
    r = int(b,3)
    if r <=679:
        m.append(r)
print(max(m))

# g = sum(map(int,b))