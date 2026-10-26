# 2 условия: 1.) 1 число повторяется 3 раза, остальные числа не повторяются
# 2.) утроенная сумма неповторяющихся чисел <= произведения повторяющихся
f = open('170.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    a3=[x for x in a if a.count(x)==3]
    a1=[x for x in a if a.count(x)==1]
    if len(a3) == 3 and len(a1) == 3 and 3*sum(a1) <= a3[0]**3:
        k +=1
print(k)
