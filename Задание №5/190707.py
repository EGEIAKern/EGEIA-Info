m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if n%2 == 0:
        b = '1' + b + '1'
    else:
        b = '1' + b + '10'
    r = int(b,2)
    if r < 65:
        m.append(r)
print(max(m))