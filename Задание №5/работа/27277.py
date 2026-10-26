m = []
def C3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x//3
    return s
for n in range(1,1000):
    b = C3(n)
    if n % 3 !=0:
        b = '1' + b + b[-3:]
    else:
        b = b + C3((b.count('1') + b.count('2'))*8)
    r = int(b,3)
    if 1100 < r < 1300:
        print(r,n)
