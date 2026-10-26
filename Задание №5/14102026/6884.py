m = []
def C12(x):
    s = ''
    d = '0123456789ab'
    while x >0:
        s = d[x%12] +s
        x = x//12
    return s
for n in range(11,1000):
    b = C12(n)
    if n %12 == 0:
        b = b + C12(n)[-2:]
    else:
        b= b + C12(9*(n %12))
    r = int(b,12)
    if r > 300:
        m.append(r)
print(min(m))