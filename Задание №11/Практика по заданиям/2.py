from math import *
for l in range(1,100000):
    kod = 4065+10+26
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 153_897 * byte > 12*1024**2:
        print(l)
        break