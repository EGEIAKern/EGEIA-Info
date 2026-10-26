m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if b.count('1')%2==0:
        b = b + '01'
        b = '101' + b[3:]
    else:
        b = b + '10'
        b = '111' + b[3:]
    r = int(b,2) # двоичное в десятичное число
    if r < 385:
        m.append(n)
print(max(m))