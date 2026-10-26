from itertools import *
def f(x,y,w,z):
    return (((x <= (not x)) and y) == w) and z
for a in product([0,1], repeat=5):
    table = [(1,a[0],0,a[1]),(a[2],1,0,0),(a[3],0,0,a[4])]
    if(len(table)) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r)))for r in table] == [1,1,1]:
                print(p)
