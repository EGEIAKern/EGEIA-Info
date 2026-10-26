# максимальная длина
from math import *
for l in range(1000,1,-1):
    kod = 120+10
    bit = ceil(log2(kod))
    byte = ceil(l*bit/8)
    if 12_755_226 * byte <= 5*1024**3:
        print(l)
        break