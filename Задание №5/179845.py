m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if (b.count('1'))%2==0:
        b = b + '0'
        b = '10' + b[2:]
    else:
        b = b + '1'
        b = '11' + b[2:]
    r = int(b,2)
    if r <19:
        m.append(n)
print(max(m))
