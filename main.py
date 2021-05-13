import configparser;config=configparser.ConfigParser();config.read('/etc/bycalc/config.ini')	# Чтение конфига
import math
(sr)=(int(config['config']['show_readme']))
(dc)=(int(config['config']['doing_circle']))	# Переводим данные в конфиге сюда
(it)=(int(config['config']['indent']))
(ir)=(int(config['config']['ignore_err']))
(xx)=(str(config['config']['name1st_num']))
(yy)=(str(config['config']['name2nd_num']))
(wp)=(str(config['config']['wdo_print']))
(ep)=(str(config['config']['error_print']))
ys=1
i=1
if sr==1:
	print('addition-"+"				subtractiont-"-"')
	print('multiplication-"*"			division-"/"')
	print('exponentiation-"**"')
	print('convert to hexadecimal code-"h"		convert to octal code-"o"')
	print('convert to binary-"b"')
	print('Config file of ByCalc in /etc/bycalc/config.ini')
	print('Github: https://github.com/madreyk/bycalc')
actions=['+', '-', '*', '/', '**', 'h', 'hex', 'hexadecimal', 'oct', 'o', 'octal', 'b', 'bin','binary']
while i==1:	# Зацикливаем
	if it>=1:	# Делаем отступ, если нужно
		print()
	x=input(xx + '=')	# Первое число
	if x=='q' or x=='quit' or x=='00':
		exit()
	wdo=input(wp)
	if wdo=='q' or wdo=='quit' or wdo=='00':
		exit()

	if wdo not in actions:	# Проверка действия
		print(ep)	# Сообщение об ошибке
		ys=0	# Запрещает идти к Y
		if it==1:	# Отступ, если нужно
			print()
		if ir==0:	# Выход, если не нужно игнорировать ошибки
			exit()
	if wdo=='h' or wdo=='hex' or wdo=='hexadecimal' or wdo=='o' or wdo=='oct' or wdo=='octal' or wdo=='b' or wdo=='bin' or wdo=='binary':
		ys=0
	if ys==1:	# Если можно идти к Y, идти
		y=input(yy + '=')	# Ввод Y
		if y=='q' or y=='quit' or y=='00':
			exit()

		if wdo=='+':	# Если +, складывать
			if it==2:	# Если нужно делать дополнительный отступ - делать
				print()
			print(x, '+', y, '=', int(x)+int(y))	# Результат
		if wdo=='-':
			if it==2:
				print()
			print(x, '-', y, '=', int(x)-int(y))
		if wdo=='*':
			if it==2:
				print()
			print(x, '*', y, '=', int(x)*int(y))
		if wdo=='/':
			if it==2:
				print()
			print(x, '/', y, '=', int(x)/int(y))
		if wdo=='**':
			if it==2:
				print()
			print(x, '**', y, '=', int(x)**int(y))
	if wdo=='h' or wdo=='hex' or wdo=='hexadecimal':
		if it==2:
			print()
		print(x, 'in hexadecimal - ', hex(int(x)))
	if wdo=='o' or wdo=='oct' or wdo=='octal':
		if it==2:
			print()
		print(x, 'on octal - ', hex(int(x)))
	if wdo=='b' or wdo=='bin' or wdo=='binary':
		if it==2:
			print()
		print(x, 'in binary - ', bin(int(x)))
	if dc==0:
		if it==1:
			print()
		exit()