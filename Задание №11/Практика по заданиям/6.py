from math import *
for kod in range(10000,1,-1):
    bit = ceil(log2(kod))
    byte = ceil(155*bit/8)
    if 202_303 * byte <= 41*1024**2:
        print(kod)
        break