x = 7**103+20*7**204-3*7**57+97
k6 = 0
while x>0:
	if x % 7 == 6: k6+=1
	x = x//7
print(k6)
x = 7 ** 103 + 6 * 7 ** 104 - 3 * 7 ** 57 + 98
a = []
while x > 0:
	a = [x % 7] + a
	x = x // 7
print(sum(a))
x = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 76
k5 = 0
k0 = 0
while x > 0:
	if x % 6 == 5:
		k5 += 1
	elif x % 6 == 0:
		k0 += 1
	x = x // 6
print(k0 - k5)

x = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 76
a = []
while x > 0:
	a = [x % 6] + a
	x = x // 6
print(a.count(0) - a.count(5))

x = 17 ** 5 + 85 ** 8 - 10
a = []
while x > 0:
	a = [x % 17] + a
	x = x // 17
print(a.count(16))

x = 7 ** 2 + 49 ** 4 - 21
a = []
while x > 0:
	a = [x % 14] + a
	x = x // 14
print(a.count(10) + a.count(0))

x = 77 * 81 ** 2031 + 23 * 729 ** 1037 - 7 * 9 ** 3023
k = 0
while x > 0:
	if (x % 81) % 4 == 0: k += 1
	x = x // 81
print(k)

x = 77 * 81 ** 2031 + 23 * 729 ** 1037 - 7 * 9 ** 3023
a = []
while x > 0:
	a = [x % 81] + a
	x = x // 81
print(len([d for d in a if d % 4 == 0]))

x = 17 * 125 ** 453 + 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
k = 0
while x > 0:
	if x % 125 < 37: k += 1
	x = x // 125
print(k)

x = 17 * 125 ** 453 + 117 * 5 ** 231 - 3 * 5 ** 13 - 2357
a = []
while x > 0:
	a = [x % 125] + a
	x = x // 125
print(len([d for d in a if d < 37]))

for x in range(1, 1000):
	a = 81 ** 20 - 9 ** x + 50
	s = 0
	while a > 0:
		s = s + a % 9
		a = a // 9
	if s == 138:
		print(x)

for x in range(1, 1000):
	a = 81 ** 20 - 9 ** x + 50
	s = []
	while a > 0:
		s = [a % 9] + s
		a = a // 9
	if sum(s) == 138:
		print(x)

for x in range(1, 10000):
	a = 64 ** 12 - 8 ** 14 + x
	k1 = 0
	k7 = 0
	while a > 0:
		if a % 8 == 1:
			k1 += 1
		elif a % 8 == 7:
			k7 += 1
		a = a // 8
	if k1 == 1 and k7 == 12:
		print(x)
		break

for x in range(1, 1000):
	a = 64 ** 12 - 8 ** 14 + x
	s = []
	while a > 0:
		s = [a % 8] + s
		a = a // 8
	if s.count(1) == 1 and s.count(7) == 12:
		print(x)
		break
m = 0
for x in range(1, 3001):
	a = 4 ** 210 + 4 ** 110 - x
	k0 = 0
	while a > 0:
		if a % 4 == 0: k0 += 1
		a = a // 4
	if k0 >= m:
		print(k0,x)
		m = k0

for x in '0123456789abcdefgh': #!!!!!!!!!!!!!!!!!
	a = int(f'9009{x}',18) + int(f'2257{x}',18)
	if a % 15== 0:
		print(x,a//15)
from string import *
for x in printable[:21]:
	a = int(f'82934{x}2',21) + int(f'2924{x}{x}7',21) + int(f'67564{x}8',21)
	if a % 20 == 0:
		print(x, a//20)
from string import *
for x in printable[1:22]:
	for y in printable[:13]:
		a = int(f'{x}23{x}5',22) - int(f'67{y}9{y}',13)
		if a % 57 == 0:
			# print(x,y,a//57) #результат без проверки суммы (можно предположить, но лучше проверить)
			# print(int(x, 22), int(y, 13), a // 57) #числа с одинаковым основанием для суммы
			print(int(x, 22) + int(y, 13), a // 57) #готовая сумма
# Ответ: 25871

from string import *
for x in printable[:17]:
	for y in printable[:17]:
		a = int(f'7{x}589{y}',17) + int(f'EE{x}{y}9AC',17)
		if a % 13==0:
			print(x,y,a//13)
# Ответ: 28406992

for x in range(130):
	a = 2*130**4+3*130**3+x*130**2+3*130+2 + 3*130**4+x*130**3+2*130**2+5*130+3
	if a % 23==0:
		print(x,a//23)



def C10(a,n):
	a = a[::-1]
	s = 0
	for i in range(len(a)):
		s = s + a[i]*n**i
	return s
for x in range(68):
	a = C10([1,2,3,x,5],68) + C10([1,x,2,3,3], 68)
	if a % 12 == 0:
		print(x,a//12)


def C10(a,n):
	a = a[::-1]
	s = 0
	for i in range(len(a)):
		s = s + a[i]*n**i
	return s

for x in range(57):
	for y in range(57):
		a= C10([5,3,x,6,6,y,3,5],57)
		if a % 56 == 0 and (y * 57 + x) **0.5%1 == 0:
			print(y * 57 + x, x*57+y)


def C10(a,n):
	a = a[::-1]
	s = 0
	for i in range(len(a)):
		s = s + a[i]*n**i
	return s
for p in range(10,30): #число 10 есть
	for x in range(1,p): # x стоит в начале числа
		for y in range(1,p):
			if C10([3,4,x,5],p) + C10([x,9,x,3],p) == C10([y,y,6,8],p):
				print(p,x,y,C10([y,x,x,y],p))

















































































































































































