from string import *
for x in printable[:18]:
    a = int(f'AB5{x}3',18) + int(f'EF{x}13',18)
    if a % 17 == 0:
        print(x,a//17)