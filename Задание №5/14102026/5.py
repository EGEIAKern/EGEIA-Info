m = []
for n in range(1,1000):
    b = bin(n)[2:]
    if len(b)%2==0:
        b = b[:len(b)//2]+ '1' + b[len(b)//2:]
    else:
        b == b
    r = int(b,2)
    if r <=26:
        m.append(n)
print(max(m))