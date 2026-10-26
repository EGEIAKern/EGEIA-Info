from math import *
for l in range(1,10000):
    kod = 10+26+8160
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 132_465 * byte > 10*1024**2:
        print(l)
        break