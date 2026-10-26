m = []
def C3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x//3
    return s
for n in range(1,1000):
    b = C3(n)
    if n % 3 == 0:
        b = '1' + b + '02'
    else:
        b = b + C3((n%3)*5)
    r = int(b,3)
    if r >= 177:
        m.append(n)
print(min(m))
