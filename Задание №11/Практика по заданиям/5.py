from math import *
for kod in range(100000,1,-1):
    bit = ceil(log2(kod))
    byte = ceil(114*bit/8)
    if 256_473 * byte <= 48*1024**2:
        print(kod)
        break