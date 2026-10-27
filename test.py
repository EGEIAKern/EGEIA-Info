from itertools import *
def f (x,y,z):
    return (not(z or x) or y and not(x) and (z and y <=z))
for a in product([0,1],repeat=5):
    table = [(a[0],a[1],a[2]),(1,a[3],1),(1,a[4],0)]
    if len(table) == len(set(table)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p,r)))for r in table] == [1,1,1]:
                print(p)