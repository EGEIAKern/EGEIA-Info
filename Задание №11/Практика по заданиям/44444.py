from math import *
for kod in range(1,1000):
    bit = ceil(log2(kod))
    byte = ceil(440*bit/8)
    if 1_892_412 * byte >= 305_726*1024:
        print(kod)
        break