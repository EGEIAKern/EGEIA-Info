# минимальная длина
from math import *
for l in range(1,10000):
    kod = 26+34+10
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 1142 * byte > 305*1024:
        print(l)
        break