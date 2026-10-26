m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if b.count('1')%2 != 0:
        b = b + '01'
    else:
        b = b + '10'
    r = int(b,2)
    if r > 123:
        m.append(r)
print(min(m))