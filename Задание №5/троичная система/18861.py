m = []
def C3(x):
    s = ''
    while x>0:
        s = str(x%3) + s
        x = x//3
    return s
for n in range(4,1000):
    b = C3(n)

    if b[-2:] == '10':
        b = '2' + b
    else:
        b = '1' + b
    r = int(b,3)
    if r > 130:
        m.append(n)
print(min(m))