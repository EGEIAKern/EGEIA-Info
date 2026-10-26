f = open('31506.txt')
k = 0
for s in f:
    a = sorted([int(x)for x in s.split()])
    if len(set(a)) == len(a) and (max(a) + min(a))*2 >sum(a) - max(a) - min(a):
        k +=1
print(k)