"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001
года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv, re

with open("Crimes.csv") as file:
	list = [crime[5] for crime in filter(lambda x: re.match(r'.*2015', x[2]), csv.reader(file))]
	print(max(set(list), key=list.count))
