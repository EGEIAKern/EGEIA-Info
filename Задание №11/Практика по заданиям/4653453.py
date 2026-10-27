from math import *
for l in range(1,10000):
    kod = 510+10
    bit = ceil(log2(kod))
    byte = ceil(bit*l/8)
    if 18_982_657 * byte >= 9379*1024*1024:
        print(l)
        break
