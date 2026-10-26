def f(n):
    b = bin(n)[2:]
    b = b + bin(n%3)[2:].zfill(2)
    r = int(b,2)
    b = b + bin(r%5)[2:].zfill(3)
    r = int(b,2)
    return r

st = 1_111_111_110 //32
end = 1_444_444_446 // 32

for i in range(st-100,st+100):
    if f(i) >= 1_111_111_110:
        print(i)
        res1 = i
        break

end = 1_444_444_446 // 32
for i in range(end+100,end-100,-1):
    if f(i) <= 1_444_444_446:
        print(i)
        res2 = i
        break
# результат 2 - результат 1 (ответ)
print(res2-res1)
