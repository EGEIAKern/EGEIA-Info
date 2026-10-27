from string import *
for x in printable[:22]:
    a = int(f'27{x}98966',22) + int(f'26{x}33',22) + int(f'522{x}5',22)
    if a % 21 == 0:
        print(x,a//21)