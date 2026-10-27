a = 1024**789 + 256**678 - 64**567
s = []
while a > 0:
    s = [a%5] + s
    a = a//5
print(s.count(4))

a = 1024**789 + 256**678 - 64**567
k = 0
while a > 0:
    if a % 5 == 4: k+=1
    a = a// 5
print(k)