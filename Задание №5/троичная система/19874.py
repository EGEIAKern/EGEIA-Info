m = []
def C3(x):
    s = ''
    while x>0:
        s = str(x%3) +s
        x = x//3
    return s
for n in range(9,1000):
    b = C3(n)
    if n%4==0:
        b = b + b[-3:]
    else:
        b = '1' + b +'20'
    r = int(b,3)
    if r > 423:
        m.append(r)
print(min(m))