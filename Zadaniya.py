import random
import math
def f54a():
	a = int(input('Введите число - '))
	b = int(input('Введите число - '))
	c = int(input('Введите число - '))
	if a<5 and b<5 or a<5 and c<5 or b<5 and c<5:
		print('Yes')
	else:
		print('No')

def f68a():
	a = int(input('a равно - '))
	b = int(input('b равно - '))
	c = int(input('c равно - '))
	d = b**2 - 4*a*c
	if d>0:
		g = (-b + math.sqrt(d))/(2*a)
		z = (-b - math.sqrt(d))/(2*a)
		print('x1 равно - ', g)
		print('x2 равно - ', z)
	elif d==0:
		x = (-b)/2*a
		print(x)
	else:
		print('Не имеет корней')

def f90a():
	b = 0
	for i in range(3,112,2):
		a = math.cos(i/(i+2))
		b += a
	print(b)

def f98a():
	print("а")
	a = 10
	b = 0.1
	for i in range(2, 11):
		a = a + a*b
		print('За ',i,'дней, лыжник пробежал - ', a)

	print("б")
	a = 10
	b = 0.1
	c = a
	for i in range(1, 7):
		a = a + a*b
		c += a
	print('В сумме за 7 дней, лыжник пробежал - ',c)

	print("в")
	a = 10
	b = 0.1
	c = a
	n = int(input('Введтие кол-во дней - '))
	for i in range(1, n):
		a = a + a*b
		c += a
	print("В сумме за", n,'дней, лыжник пробежал - ', c)

	print("г")
	a = 10
	b = 0.1
	n = 1
	while a <= 80:
		a = a + a*b
		n += 1
	print('На',n-1 ,'день, ему стоит прекратить увеличивать пробег')

def f4b():
	x = int(input('Введите первый элемент арифметической прогрессии - '))
	n = int(input('Введите последний элемент арифметической прогрессии - '))
	d = int(input('Введите разность - '))
	for i in range(x, n, d):
		print(i)

def f16b():
	a = [random.randint(-4,3) for i in range(7)]
	z = []
	b = []
	for i in range(0,len(a)):
		if a[i]>=0:
			b.append(a[i])
		else:
			z.append(a[i])
	print(len(b), len(z))
	for i in range(len(a)):
		if len(z)<len(b):
			z.append(-1)
		elif len(b)==len(z):
			break
		elif len(z)>len(b):
			b.append(1)	
	a = b+z
	random.shuffle(a)
	print(a)

def f8a():
	a = 2
	b =3 
	print((a+4*b)*(a-3*b)+a**2)

def f25a():
	a = int(input('Введите кол-во недель - '))
	b = int(input('Введите кол-во месяцев - '))
	c = int(input('Введите кол-во лет - '))
	a = a*7
	b = b*30
	c = c*360
	print(a, b, c)

def f40a():
	a = int(input('Введите число - '))
	if -10<a<10:
		print(a+5)
	else:
		print(a-10)

def f71a():
	h= int(input('Введите кол-во часов - '))*60
	m = int(input('Введите кол-во минут'))
	a = h+m
	j = a/2
	k = m*6
	k = k-j
	print('Градус между стрелками равен - ',abs(k))

def f6b():
	a = [random.randint(1,100) for i in range(25)]
	b = []
	for i in range(0, len(a)):
		if a[i]%3==0:
			b.append(a[i])
	b.sort(reverse = True)
	print(b)

def f37a():
	a = int(input())
	b = int(input())
	print(max(a,b))
	
def f41a():
	a = int(input())
	if 100<a or a<-100:
		print(0)
	else:
		print(a+1)
	
def f43a():
	a = int(input())
	if a == 12 or a==1 or a==2:
		print('Зима')
	elif a==3 or a==4 or a==5:
		print('Весна')
	elif a==6 or a==7 or a==8:
		print('Лето')
	elif a >12:
		print('Error')
	else:
		print('Осень')
		
def f84a():
	for i in range(1,101):
		a = i*74
		print(i,'$',' - ',a,'Руб.',' - ',a/20,'Кг. конфет')
	
def f7b():
	a = 1
	b = 1
	for i in range(15):
		a,b = b, a+b
		print(b)

def f26b():
	a = [1,3,5,7,9,11,13,5,6]
	b = []
	c = []
	p = 0
	for i in range(len(a)):
		b.append(a[i])
		c.append(a[i])
		if a[i]%2==0:
			del b[-1]
			p = sum(b)
			print(p)
			break	
	if p == False:
		del c[0]
		del c[-1]
		print(sum(c))
	
def f9a():
	x = -2
	print(abs(x)+x**5)	
	
def f57a():
	a = [int(input('Введите день - ')), int(input('Введите месяц - ')), int(input('Введите год - '))]
	if a[1] == 2 and a[0] > 28:
		print('Такой даты нет!')
	elif a[0] > 31 and a[1] >12:
		print('Такой даты нет!')
	else:
		print('Такая дата существует!')

def f75a():
	print("You are welcome!"*10)

def f81a():
	a = 100
	while a>=0:
		print(a)
		a -= 4

def f8b():
	def chek(x):
		for n in range(2,x):
			if x%n == 0:
				return False
			return True


	mass = []
	while True:
		a = int(input('Введите начало массива - '))
		b = int(input('Введите конец массива - '))
		if a != 0:
			break
		else:
			print('Wasted')
	for i in range(a,b):
		if chek(i) == True:
			mass.append(i)
	print(mass)

def f27a():
	a = int(input('Введите число - '))
	b = int(input('Введите число - '))
	c = int(input('Введите число - '))
	h = [a, b, c]
	a += b
	b = c - h[0]
	c = h[0] + h[1] + c
	print('A равно - ', a,', ', 'B равно - ', b,', ','C равно - ', c)

def f80a():
	for i in range(1001, 1026,3):
		print(i)

def f29b():
	n = int(input())
	p = 1
	for i in range(2, n+1):
		if i%2==0:
			p -= i
		else:
			p += i
		print(p)

def f77a():
	n = int(input('Введите кол-во строк - '))
	for i in range(5):
		print('0'*n)

def f78a():
	n = int(input('Введите сторону квадрата - '))
	for i in range(n):
		print('*'*n)


while True:
	n = int(input('Выберите: Вычесления(1)/Массивы(2) - '))
	if n == 1:
		x = int(input('Введите номер задания - '))
		if x == 54:
			f54a()
		if x == 68:
			f68a()
		if x == 90:
			f90a()
		if x == 98:
			f98a()
		if x == 8:
			f8a()
		if x == 25:
			f25a()
		if x == 40:
			f40a()
		if x == 71:
			f71a()
		if x == 37:
			f37a()
		if x == 41:
			f41a()
		if x == 43:
			f43a()
		if x == 84:
			f84a()
		if x == 9:
			f9a()
		if x == 57:
			f57a()
		if x == 75:
			f75a()
		if x == 81:
			f81a()
		if x == 27:
			f27a()
		if x == 80:
			f80a()
		if x == 77:
			f77a()
		if x==78:
			f78a()
	if n == 2:
		x = int(input('Введите номер задания - '))
		if x == 4:
			f4b()
		if x == 16:
			f16b()
		if x == 6:
			f6b()
		if x == 7:
			f7b()
		if x == 26:
			f26b()
		if x == 8:
			f8b()
		if x == 29:
			f29b()
