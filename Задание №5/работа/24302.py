m = []
def C3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x//3
    return s
for n in range(1,100000):
    b = C3(n)
    if b.count('1') + b.count('2') % 9 ==0:
        b = b + '2'
    else:
        b = C3(b.count('1') + b.count('2') % 9)
    r = int(b,3)
    if n > 166:
        m.append(r)
print(min(m))
