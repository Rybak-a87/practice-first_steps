#Практика (Д/З)
from test_time import *
import os



# Урок 7 (Python с нуля) (работа со строками)
#@test_time
def prac7_1(): #подсчет букв "а"
	z = ("a")
	a = ("abrakadabra")
	res = 0
	for i in range(0, len(a)):
		if z in a[i]:
			res += 1
	print(res)


#@test_time
def prac7_1v2(): #подсчет букв "а" (с помощью метода)
	z = ("a")
	a = ("abrakadabra")
	print(a.count(z))


#@test_time
def prac7_2(): #удаление всех сочетаний "ab"
	a = ("abrakadabra")
	b = (a[2:7] + a[9:])
	print(b)


#@test_time
def prac7_2v2(): #удаление всех сочетаний "ab" (с помощью метода)
	a = ("abrakadabra")
	b = a.replace("ab", "")
	print(b)


#@test_time
def prac7_3(): #определение слова палиндром
	a = input("Введите слово: ")
	if a == a[::-1]:
		print(f"Слово {a} является палиндромом!")
	else:
		print(f"Слово {a} не палиндром!")


#@test_time
def prac7_4(): #определение колличества фраз "ra"
	z = ("ra")
	a = ("abrakadabra")
	res = 0
	for i in range(0, len(a)):
		for j in range(i, len(a) + 1):
			if a[i:j] == z:
				res += 1
			else:
				continue
	print(res)


#@test_time
def prac7_4v2(): #определение колличества фраз "ra" (с помощью метода)
	z = ("ra")
	a = ("abrakadabra")
	print(a.count(z))


#@test_time
def prac7_5(): #разделения предложения на слова
	a = input("Введите предложение: ")
	for i in range(0, len(a)):
		if a[i] != " ":
			print(a[i], end = "")
		else:
			print()
			continue
	print()


#@test_time
def prac7_5v2(): #разделения предложения на слова 2й способ (с помощью метода)
	a = input("Введите предложение: ").split()
	for i in range(0, len(a)):
		print(a[i])



# Урок 8 (Python с нуля) (методы строк)
#@test_time
def prac8_1(): #корректный ввод номера телефона по шаблону х(ххх)хххххх
	err = ("Ввод не соответствует формату х(ххх)хххххх\nПопробуйте еще раз: ")
	while True:
		a = input("Введите номер телефона в формате х(ххх)хххххх\n")

		if a in "quit":
			exit()
		elif len(a) == 12:
			if a[1] in "(" and a[5] in ")":
				b = a.replace("(", "").replace(")", "")
				if b.isdigit():
					print(f"Спасибо, введенный Вами номер телефона {a} является корректным!")
				else:
					print(err)
			else:
				print(err)
		else:
			print(err)


#@test_time
def prac8_2(): #в строку "2+3+6.7 + 82 + 5.7 +1" заменить + на - и удалить все пробелы
	a = ("2+3+6.7 + 82 + 5.7 +1")
	b = a.replace(" ", "").replace("+", "-")
	print(b)


#@test_time
def prac8_3(): #вывести числа 0; -100; 5.6; -3 в виде столбца по правому краю
	a = ("0; -100; 5.6; -3")
	b = a.replace(";", "").split()
	for i in range(len(b)):
		print(b[i].rjust(20))


#@test_time
def prac8_4 (): #в строке "abrakadabra" найти "ra" и вывести их индексы
	z = ("ra")
	a = ("abrakadabra")
	q = a.count(z)
	print(f"В слове {a} - {z} встречается {q} раза")
	print(f"Индекс {z} в слове {a}: ", end = "")
	y = a.find(z)
	for i in range(q):
		print(a.find(z, y), end = "; ")
		y = a.find(z, y) + 1
	print()



# Урок 9 (Python с нуля) (списки и функции)
#@test_time
def prac9_1(): #увеличить каждый элемент списка [-1, 0, 5, 3, 2] на 7.2
	a = [-1, 0, 5, 3, 2]
	k = 7.2
	for i in range(len(a)):
		a[i] += k
	print(a)


#@test_time
def prac9_2(): #пользователь вводит значения, на их основе сформировать список состоящий из продублированных значений
	n = int(input("Сколько элементов будет в списке?: "))
	d = int(input("Сколько клонов необходимо?: "))
	a = [0] * d
	c = []
	for i in range(n):
		b = input(f"Введите {i + 1}й элемент списка: ")
		for j in range(d):
			a[j] = b
		c += a
	print(c)


#@test_time
def prac9_3(): #сложить две матрицы

	m1 = [[1, 3, 5], [2, 4, 6]]
	m2 = [[1, 0, 1], [0, 1, 1]]
	a = [[0, 0, 0], [0, 0, 0]]

	if len(m1) >= len(m2):
		dl = len(m1)
	else:
		dl = len(m2)

	for i in range(dl):

		if len(m1[i]) >= len(m2[i]):
			dll = len(m1[i])
		else:
			dll = len(m2[i])

		for j in range(dll):

			a[i][j] = (m1[i][j] + m2[i][j])


	print(m1)
	print(m2)
	print("SUMM")
	print(a)


#@test_time
def prac9_4(): #пользователь вводит значения в список, в нем проверить была ли введена циара 5
	n = int(input("Сколько элементов будет в списке?: "))
	a = [0] * (n)


	for i in range(n):
		b = input(f"Введите {i + 1}й элемент списка: ")
		a[i] = b

	b = input("Введите элесент который необходимо найти: ")
	if b in a:
		print(f"Элемент {b} есть в списке!")
	else:
		print("Извените данного элемента нет в списке.")



# Урок 10 (Python с нуля) (списки, срезы и методы)
#@test_time
def prac10_1(): #пользователь вводит числа, до тех пор пока не введен 0. Все введенные числа возводятся в квадрат и помещаются в список
	s = []
	while True:
		a = (int(input("Введите целое число: ")))
		t = [0] #1
		if a == 0:
			print("Вы ввели  0, программа остановлена")
			break
		else:
			#a **= 2 #1
			#t[0] = a #1
			#s += t #1
			s.append(a**2) #2
	print(f"ВВеденные вами числа возведенны в квадрат и помещены в список:\n{s}")


#@test_time
def prac10_2(): #удалять из списка ["+7912123456", "+715213456", "+6915213456", "+4915213456", "+7915213456"] номера на +7
	s = ["+7912123456", "+715213456", "+6915213456", "+4915213456", "+7915213456"]
	d = ("+7")
	ss = []
	print(f"Первоначальный список: {s}")
	for i in range(len(s)):
		if d not in s[i][:2]:
			ss.append(s[i])
	print(f"Обработанный список: {ss}")


#@test_time
def prac10_3(): #сдвигает любой элемент списка в начало или конец списка (2 способа: цикл и методы)
	a = [1, 2, 3, 4, 5, 6]
	print(f"Есть список\n{a}")
	e = int(input("Какой элемент хотите переместить: "))
	if e in a:
		ind = a.index(e)
		t = a.pop(ind) #2
		r = input("Влево (l) или вправо (r)")
		if r in "r":
			#for i in range(ind, len(a) - 1): #1
				#a[i], a[i + 1] = a[i + 1], a[i] #1
			a.append(t) #2
			print(a)
		elif r in "l":
			#for i in range(ind, 0, -1): #1
				#a[i], a[i - 1] = a[i - 1], a[i] #1
			a.insert(0, t) #2
			print(a)
		else:
			print("Что-то пошло не так..., не правильный ввод")
	else:
		print("В списке нет такого элемента")



#Урок 12 (Python с нуля) (словари, их методы)
#@test_time
def prac12_1(): #вводим произвольные целые числа, ключами будут только четное числа, а значениями - квадраты этих чисел
	s = {}
	r = 1
	ch = []
	k = []
	while r:
		a = int(input("Введите целое число: "))
		if a != 0:
			ch.append(a)
		if a == 0:
			r = 0
		elif a%2 == 0:
			k.append(a) #1 добавление ключей в список
			#if a not in s: #1
				#s[a] = a ** 2 #1
			s.setdefault(a, a ** 2) #2
	#for i in s.keys(): #2 добавление ключей в список
		#k.append(i) #
	print(f"Вы ввели:\n{ch}")
	print(f"Числа которые подошли:\n{k}")
	print(f"Это ваш словарь:\n{s}")


#@test_time
def prac12_2():#из строки "int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип" сделать словарь
	s = ("int=целое число, dict=словарь, list=список, str=строка, bool=булевый тип")
	a = s.replace("=", ", ").split(", ")
	#l = [] #3
	d = {}
	for i in range(0, len(a), 2):
		#d[a[i]] = a[i + 1] #1
		d.setdefault(a[i], a[i + 1]) #2
		#l1 = [] #3
		#l1.append(a[i]) #3
		#l1.append(a[i+1]) #3
		#l.append(l1) #3
	#d = dict(l) #3
	print(f"Изначальная строка:\n{s}")
	print(f"Словарь из строки:\n{d}")


#@test_time
def prac12_3(): #переводчик - английское слово (ключ), руссное (значение)
	s = {}
	x = 0
	N = int(input("Сколько слов добавим в словарь?: "))
	os.system("cls")
	while x < N:
		a = input("Введите слово на английском языке и перевод на русском в формате (слово на английском: перевод1, перевод2, ..., переводN): ")
		ta = list(a)
		if "quit" in a:
			os.system("cls")
			print("Программа остановлена")
			exit()
		elif ta.count(":") == 1:
			tl = a.split (":")
			if tl[0] not in s:
				#s[tl[0]] = tl[1] #1
				s.setdefault(tl[0], tl[1]) #2
				x += 1
				os.system("cls")
			else:
				os.system("cls")
				print(f"Ввод {tl[0]} повторяется")
		elif ta.count(":") > 1:
			os.system("cls")
			print("Ввод не соответствуе формату ввода, много двоеточий")
		else:
			os.system("cls")
			print("Ввод не соответствуе формату ввода, нет двоеточия")

	print(f"Введенные вами данные приобразованы в словарь:\n{s}")



#Урок 13 (Python с нуля) (Кортежи и операции с ними)
#@test_time
def prac13_1(): #дан кортеж ("+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558") вывести все номера на +7
	p = ("+792345678", "+792345478", "+792355678", "+592345678", "+392345678", "+7923456558")
	s = ("+7")
	a = []
	for i in range(len(p)):
		if s in p[i][:2]:
			a.append(p[i])
	b = tuple(a) #преобразования списка в кортеж
	print(f"Из кортежа:\n{p}")
	print(f"Номера с {s}:\n{b}")


#@test_time
def prac13_2(): #есть строка "Оценки: 5, 4, 3, 4, 2, 4, 5, 4" создать кортеж только с оценок в виде целых чисел
	o = []
	s = ("Оценки: 5, 4, 3, 4, 2, 4, 5, 4")
	#a = s.replace(" ", "").replace(",", "") #1
	#l = a.split(":") #1
	#for i in range (len(l[1])): #1
	#	o.append(int(l[1][i])) #1
	for i in range(len(s)): #2 (более автоматизирует программу)
		if s[i].isdigit(): #2
			o.append(int(s[i])) #2
	p = tuple(o)
	print(f"Из строки:\n{s}")
	print(f"Отделены оценки в виде целых чисел в картеж:\n{p}")


#@test_time
def prac13_3(): #вывести значение кортежа ((1,2,3)(4,5,6)(7,8,9)) в виде таблицы 1 - 2 - 3 и т.д.
	p = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
	print(f"Из кортежа:\n{p}")
	print("Получилась таблица:")
	for i in range (len(p)):
		a = str(p[i])
		#b = a.replace(",", " -").replace("(", "").replace(")", "") #1
		z = [] #2
		for j in range(len(a)): #2 поиск в списке цифр (типа автоматизировал программу)
			if a[j].isdigit(): #2
				z.append(a[j]) #2
		#print (b) #1
		print(f"{z[0]} - {z[1]} - {z[2]}") #2


'''

Урок 14 (Python с нуля) (Функции. Начало)

Урок 15
Реализовать подобным образом игру "Крестики-нолики"
'''
'''Урок 16 (Рекурсивные и лямбда-функции, функции с произвольным числом аргументов)
1. Написать рекурсивную функцию для вычисления факториала числа n: n != 1*2*3*...*n
2. Написать функцию для вычисления среднего арифметического переданных ей значений 
	в виде аргументов: arg1, arg2, ...,argN
3. Реализовать функцию сортировки выбранных элементов по возрастанию: элементы передают 
	функции в виде списка и выбираются они с помощью функции-селектора, указанной в 
	качестве второго параметра. Привести примеры вызова функции сортировки с разными 
	видами селекторов. Селекторы реализовать в виде лямбда-функции.
'''
#@test_time
def prac16_1():
	a = int(input("Введите целое число, для вычисление его факториала: "))
	def factorial(a):
		if a == 1:
			return 1
		else:
			return a * factorial(a - 1)
	print(f"Факториал числа {a} равен: {factorial(a)}")


#@test_time
def prac16_2():
	#a = input("Введите через пробел числа, для вычисления их среднего арифметического: ").split()

	def sred_arif(*args):
		s = 0
		for i in args:
			s += i
			res = s / len(args)
		print(f"Cреднего арифметического переданных {args} равно: {res}")
	sred_arif(1, 2, 4, 5 , 13)


#@test_time
def prac16_3sort():
	def app_lambda(args, fun):
		for i in range(len(args)):
			for j in range(i + 1, len(args) - 1):
				if fun(args[i], args[j]):
					args[i], args[j] = args[j], args[i]
		print(args)


	l = [1, 2, -5, 6, 3, 7]
	app_lambda(l, (lambda a, b: True if a > b else False))


#@test_time
def prac16_3max():
	def max_lambda(args, fun):
		m = args[0]
		for i in args:
			m = fun(i, m)
		print(m)
	l = [1, 2, -5, 6, 3, 7]
	max_lambda(l, (lambda i, m: i if i > m else m))



'''Урок 17 (Алгоритм Евклида, принцип тестирования программ)
1. Реализовать последний вариант алгоритма Евклида с помощью рекурсивной функции.
2. Написать функцию нахождения максимального значения среди переданных аргументов: arg1, arg2, ...,argN
3. Реализовать универсальную функцию для нахождения максимального и минимального значения среди: arg1, arg2, ...,argN
	с помощью функцию-селектора, указанной в виде лямбда-функции как один из параметров функции поиска.
'''
#@test_time
def prac17_1():
	def ifkl_recurs(a, b):
		if a < b:
			a, b = b, a
		if b > 0:
			return ifkl_recurs(b, a % b)
		else:
			return a
		#while b > 0:
			#a, b = b, a % b
	print(f"Найбольший общий делитель двух чисел - равен: {ifkl_recurs(24, 22)}")


#@test_time
def prac17_2():
	def max_arg(*args):
		m = args[0]
		for i in range(1, len(args)):
			if args[i] > m:
				m = args[i]
		print(f"Максимальное число из {args} - это {m}")
	max_arg(1, 4, 6, 345, 347, 74)


#@test_time
def prac17_3():
	def min_max(*args):
		mn = args[0]
		mx = args[0]
		for i in range(1, len(args)):
			if args[i] < mn:
				mn = args[i]
			elif args[i] > mx:
				mx = args[i]
		print(f"Максимальное значение среди {args} - является: {mx}")
		print(f"Минимальное значение среди {args} - является: {mn}")
	min_max(31, 342, 435, 234, 11, 5342)


'''Урок 19 (Множества (set) и операции над ними - вычитание, пересечение, объединение, сравнение)
Напишите программу, которая из введенного с клавиатуры текста определяет число 
	уникальных слов. Для простоты можно полагать, что слова разделяются пробелом или 
	символом переноса строки '\n'
'''
#@test_time
def prac19_1():
	a = set(input("Введите предложение: ").split())
	print(f"Колличество уникальных слов в веденном Вами предложении, составляет: {len(a)}")

'''Урок 20 (Итераторы, выражения-генераторы, функции-генераторы, оператор yield)
Пусть дан текст:
	t = ("""Генератор - это итератор, элементы которого
	можно перебирать (итерировать) только один раз.
	Итератор - это объект, который поддерживает функцию next()
	для перехода к следующему элементу коллекции.""")
Написать функцию-генератор для выделения слов из этого текста (слова разделяются 
пробелом или символом переноса строки '\n'). Список всех слов при этом в функции не создавать.
'''
@test_time
def prac20_1():
	t = """Генератор - это итератор, элементы которого
	можно перебирать (итерировать) только один раз.
	Итератор - это объект, который поддерживает функцию next()
	для перехода к следующему элементу коллекции."""
	a = (x for x in t.split())
	for i in t.split():
		print(next(a), end=" ")

'''Урок 21 (Функции map, filter, zip)
1. Поставить в соответствии соответствующим английским символам русские буквы: 
	h - х, e - е, l - л, o - о, w - в, r - р, d - д
	и преобразовать строку: "hello world!"
	в русские символы.
2.Дан текст:
	t = """Куда ты скачешь гордый конь,
	И где опустишь ты копыта?
	О мощный властелин судьбы!
	Не так ли ты над самой бездной,
	На высоте, уздой железной
	Россию поднял на дыбы?"""
	Необходимо выделить каждое второе слово из этого стихотворения и представить результат в виде 
	упорядоченного списка. (Подумайте как реализовать алгоритм с наименьшими затратами по памяти).
3.Реализовать алгоритм для нахождения всех делителей натурального числа N. Число N вводится с 
	клавиатуры. Для начала можно реализовать простым перебором всех N возможных чисел (делителей). 
	Затем подумайте, как можно оптимизировать по скорости этот алгоритм.
'''
#@test_time
def prac21_1():
	d = {"h": "х", "e": "е", "l": "л", "o": "о", "w": "в", "r": "р", "d": "д"}
	s = "hello world!"
	print(f"<<{s}>> преобразовано в русский:", end=" ") #2
	#l = [] #1
	for i in list(s):
		if i in d:
			print(d[i], end="") #2
			#l.append(d[i]) #1
		else:
			print(i, end="") #2
			#l.append(i) #1
	#res = str(l).replace("'", "").replace(", ", "").replace("[", "").replace("]", "") #1
	#print(f"<<{s}>> преобразовано в русский: <<{res}>>") #1

#@test_time
def prac21_2():
	t = """Куда ты скачешь гордый конь,
	И где опустишь ты копыта?
	О мощный властелин судьбы!
	Не так ли ты над самой бездной,
	На высоте, уздой железной
	Россию поднял на дыбы?"""
	a = list(t.replace("\n\t", " ").split(" "))
	g = (a[x] for x in range(0, len(a), 2))
	try:
		i = True
		while i:
			print(next(g), end=" ")
	except StopIteration:
		i = False


'''Урок 22 (Сортировка sort() и sorted(), сортировка по ключам)
1. Используя сортировку, найдите первые три наименьшие значения в списке: a = [1, 2, -5, 0, 5, 10]
	Сам список должен оставаться неизменным.
2. Отсортируйте список: digs = (-10, 0, 7, -2, 3, 6, -8)
	так, чтобы сначала шли отрицательные числа, а затем положительные.
3. Пусть имеется словарь: {"+7": 23445678901, "+4": 3456789012, "+5": 5678901234, "+12": 78901234}
	Необходимо вывести телефонные номера по убыванию чисел, указанных в ключах, то есть по порядку: +4, +5, +7, +12
'''
#@test_time
def prac22_1():
	a = [1, 2, -5, 0, 5, 10]
	g = (x for x in sorted(a))
	print(f"Три найменьших значения списка {a} - это: ", end="")
	for i in range(3):
		print(next(g), end=", ")

#@test_time
def prac22_2():
	def sor(a, oper): #1
		if oper == "-":
			for i in a:
				if i < 0:
					print(i, end=" ")
		elif oper == "+":
			for i in a:
				if i > 0:
					print(i, end=" ")

	digs = (-10, 0, 7, -2, 3, 6, -8)
	sor(digs, "-") #1
	sor(digs, "+") #1
	print()
	print(sorted(digs)) #2
	for i in sorted(digs):
		if i == 0:
			continue
		print(i, end=" ")

#@test_time
def prac22_3():
	d = {"+7": 23445678901, "+4": 3456789012, "+5": 5678901234, "+12": 78901234}
	def oneSort(d): #1
		i = 0
		j = 1
		while i != len(d):
			jj = (f"+{j}")
			if f"+{j}" in d:
				print(f"{jj}: {d[jj]}")
				i += 1
				j += 1
			else:
				j += 1

	def twoSort(d):
		l = []
		i = 0
		j = 1
		while i != len(d):
			jj = (f"+{j}")
			lt = []
			if jj in d:
				lt.append(f"{jj}")
				lt.append(d[jj])
				l.append(lt)
				i += 1
				j += 1
			else:
				j += 1
		d = dict(l)
		for i in reversed(d):
			print(f"{i}: {d[i]}")
	oneSort(d)
	twoSort(d)


'''Урок 23 (Обработка исключений - try, except, finally, else)
1. Напишите программу ввода натуральных чисел через запятую и преобразования этой строки в список 
	целых чисел. (Используйте здесь функцию map для преобразования элементов последовательности строк 
	в последовательность чисел). Реализовать обработку возможных исключений при таком преобразовании.
2. Написать функцию вычисления среднего арифметического элементов переданного ей списка. Реализовать 
	обработку возможных исключений при её работе.
3. Написать функцию-генератор (с использованием оператора yield) для удаления произвольного элемента 
	из множества (с помощью метода pop()). Функция должна возвращать значение удалённого элемента. 
	Реализовать обработку возможных исключений при ее работе.
'''
#@test_time
def prac23_1_2_3():
	#def forInt(a): #1
	#	return int(a) #1
	def delEl(a):
		d = a.pop()
		yield d
	while True:
		try:
			a = list(input("Введите натуральные числа через запятую: ").replace(" ", "").split(","))
			#b = map(forInt, a) #1
			b = map(lambda x: int(x), a) #2
		except ValueError:
			print("\nНекоректный ввод")
		else:
			for i in range(len(a)):
				a[i] = next(b)
			print(f"[1] - Введенные вами строка приобразована в список из чисел: {a}")
			#---------
			s = 0
			for j in a:
				s += j
			res = s / len(a)
			print(f"[2] - Среднее арифметическое введенного списка из чисел равно: {res}")
			#----------
			a = set(a)
			print(f"[3] - Приобразовуем наш список в множество: {a}")
			while True:
				z = input("Ходите удалить случайный элемент?\n(1) - Да; (2) - Нет; ")
				if z in "1":
					print(f"Удаленный элемент: {next(delEl(a))}")
					if a == set():
						print("\nЭлементы закончились")
						print("Программа завершена")
						break
					print(f"Теперь множество выглядит так: {a}")
				elif z in "2":
					print("Программа завершена")
					break
				else:
					print("Неверная команда")
		break


'''Урок 24 (Файлы - чтение и запись - open, read, write, seek, readline, dump, load, pickle)
1. Выполнить считывание данных из текстового файла через символ и записи прочитанных данных в другой текстовый файл.
	Прочитывайте там не более 100 символов.
2. Пользователь вводит предложение с клавиатуры. Разберите это предложение по словам (считать, что 
	слова разделены пробелами) и сохранить их в столбец в файл.
3. Пусть имеется словарь:
	d = {"house": "дом", "car": "машина",
	"tree": "дерево", "road": "дорога",
	"river": "река"}
	Необходимо каждый элемент этого словаря сохранить в бинарном файле как объект. Затем, прочитать этот 
	файл и вывести считанные объекты в консоль.
'''
#@test_time
def prac24_1():
	with open("files/file_full.txt", "r") as f:
		a = f.read()
		with open("files/file_test.txt", "w", encoding="utf-8") as f1:
			for i in range(0, 200, 2):
				print(a[i], end="")
				f1.write(a[i])

#@test_time
def prac24_2():
	a = input("Введите предложение: ").split()
	with open("files/file_test.txt", "w", encoding="utf-8") as f:
		for i in a:
			f.write(f"{i}\n")

#@test_time
def prac24_3():
	import pickle #библиотека для работы с винарными файлами
	d = {"house": "дом", "car": "машина",
		 "tree": "дерево", "road": "дорога",
		 "river": "река"}
	with open("files/file.bin", "wb") as f:
		for i in tuple(d):
			pickle.dump(d[i], f) #записать в бинарный файл

	with open("files/file.bin", "rb") as f:
		for i in range(len(d)):
			a = pickle.load(f) #считать с бинарного файла
			print(a)


'''Урок 25 (Форматирование строк - метод format и F-строки)
1. Пользователь через пробел вводит ФИО. На основе этой информации требуется создать строку с сообщением:
	Ваши персональные данные:
	Фамилия: введенная фамилия
	Имя: введенное имя
	Отчество: введенное отчество
2. Имеется текстовый файл с содержимым:
	Иван, ivan@gm.com, 18
	Татьяна, tat@gm.com, 22
	Сергей, srg@gm.com, 33
	Федор, fr@gm.com, 41
	Елена, el@gm.com, 27
	Необходимо построчно считывать информацию и для каждой строки для лиц не старше 30 лет сформировать сообщение:
	Уважаемый(ая) <имя>! Приглашаем Вас принять участие в курсах по изучению Python. 
	Подробную информацию мы выслали на email: <email>.
'''
#@test_time
def prac25_1():
	a = input("Введите через пробел Ф.И.О.: ").split()
	print("Ваши персональные данные:")
	print(f"Фамилия: {a[0]}\nИмя: {a[1]}\nОтчество: {a[2]}")

#@test_time
def prac25_2():
	with open("files/file25.txt", "r", encoding="utf-8") as f:
		while True:
			line = f.readline().replace(",", "").split()
			if line == list():
				break
			if int(line[2]) < 30:
				print(f"""Уважаемый(ая) {line[0]}! Приглашаем Вас принять участие в курсах по изучению Python.
Подробную информацию мы выслали на email: {line[1]}.\n""")


'''Урок 26 (Создание и импорт модулей - import, from, as, dir, reload)
1. Задайте в модуле словарь, в котором ключами являются английские слова, а значение соответствующее 
	русские (перевод). Также добавьте необходимые функции для добавления и удаления новых слов в этом 
	словаре. Импортируйте этот модуль в основную программу и реализуйте мини-словарь со следующим меню (функционалом):
	(1) Перевести слово
	(2) Добавить слово
	(3) Удалить слово
	(4) Завершить работу
2. Попробуйте развить идею словаря и добавьте возможность автоматического сохранения и считывания данных из
	файла (в файле сохраняется словарь целиком).
'''
#@test_time
def prac26_1():
	d = {"red": "красный",
		 "car": "машина",
		 "house": "дом",
		 "window": "окно",
		 "city": "город",}
	while True:
		a = input("Выбирите необходимую отерацию:\n(1) Перевести слово\n(2) Добавить слово\n(3) Удалить слово\n(4) Содержимое словаря\n(5) Завершить работу\n")
		if a in "1":
			t = input("Введите слово на английском: ")
			if t in d:
				print(f"{t} на руском - {d[t]}\n")
			else:
				print(f"Извените слова {t} нет в словаре.\n")
		elif a in "2":
			while True:
				i = input("(0) - назад в главное меню\nВведите слово на английском и через тире его перевод на русский: ").replace(" ", "")
				if "-" in i:
					d.update([i.split("-")])
					break
				elif i in "0":
					break
				else:
					print("Неверный ввод\n")
		elif a in "3":
			while True:
				for j in tuple(d):
					print(f"- {j}")
				x = input("(0) - назад в главное меню\nВведите слово из перечисленного списка для удаления: ")
				if x in "0":
					break
				elif x in tuple(d):
					d.pop(x)
				else:
					print("Неверный ввод, такого слова нет.\n")
		elif a in "4":
			print("В данном словаре содержатся следующие слова:")
			for i in tuple(d):
				print(i, end="; ")
			print("\n")
		elif a in "5":
			break
		else:
			print("Неверный ввод.\n")

'''Урок 28 (Декораторы функций и замыкания)
1. Напишите две функции создания списка из четных чисел от 0 до N (N - аргумент функции): [0, 2, 4, ..., N]
	с помощью метода append и с помощью инструмента list comprehensions (генератор списков).
	Через декоратор определите время работы этих функций.
2. Напишите декоратор для кэширования результатов работы функции вычисления квадратного 
	корня положительного целочисленного значения x. То есть, при повторном вызове функции (через декоратор) 
	с одним и тем же аргументом, результат должен браться из кэша, а не вычисляться заново. (Подсказка: 
	здесь следует использовать замыкание для хранения кэша).
'''

def prac28_1():
	#@test_time
	def funс_1(n):
		l = list()
		for i in range(0, n + 1, 2):
			l.append(i)
		print(l)

	#@test_time
	def func_2(n):
		l = [x for x in range(0, n + 1, 2)]
		print(l)

	N = 100000
	funс_1(N)
	func_2(N)

#@test_time
def prac28_2():
	def kesh(func): #Функция кэширования данных
		memo = {} #хранилище данных кэша (словарь)
		def wrapper(*args):
			if args in memo: #проверяем наличие результата функции кэше
				return memo[args]
			else: #добавляем результат функции кэш
				retFunc = func(*args)
				memo[args] = retFunc
				return retFunc
		return wrapper

	@kesh
	def func(x):
		return x * x

	res = func(4)
	print(res)