m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if n%2 == 0:
        b = '11' + b + '11'
    else:
        b = '11' + b + '00'
    r = int(b,2)
    if r > 105:
        m.append(r)
print(min(m))