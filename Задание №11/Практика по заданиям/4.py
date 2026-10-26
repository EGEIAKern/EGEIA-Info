from math import *
for kod in range(1,10000):
    bit = ceil(log2(kod))
    byte = ceil(251*bit/8)
    if 65_536 * byte >= 8064*1024:
        print(kod)
        break