from math import *
for kod in range(1,10000):
    bit = ceil(log2(kod))
    byte = ceil(36*bit/8)
    if 1_000_000 * byte >= 52*1024**2:
        print(kod)
        break