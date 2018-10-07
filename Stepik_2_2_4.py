"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
"""

f = open("dataset_24465_4.txt", "r")
fileData = f.read()
print(fileData)
arrayData = fileData.split()
print(arrayData)
a = len(arrayData) - 1
f.close()
f = open("test.txt", "w")
for i in range(len(arrayData)):
	f.write(arrayData[a])
	f.write('\n')
	a = a - 1
f.close()
