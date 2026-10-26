from itertools import *
def f(x,y,w,z):
    return(функция) #например (w≡z)∨¬(y→w)∨¬x
for a in product([0,1], repeat=3): # [0,1] - значения в таблице. repeat = 3 - количество пропусков в таблице
    table = [(1,1,0,a[0]),(a[1],1,0,0),(a[2],0,0,0), (1,1,1,1)] #значения в таблице
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r)))for r in table] == [0,0,0]: #значение F
                print(p)