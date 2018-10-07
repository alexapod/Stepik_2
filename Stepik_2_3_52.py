"""
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents,
которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не
наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""

import json


def getParentByName(parentName):
	for clazz in data:
		if clazz['name'] == parentName:
			return clazz
	return None


def findChildren(parent):
	children = set()
	for child in parent['children']:
		children.add(child)
		children = children.union(findChildren(getParentByName(child)))
	return children


data = json.loads(input())
for child in data:
	child['children'] = set()
for child in data:
	for parentName in child['parents']:
		parent = list(filter(lambda x: x['name'] == parentName, data))[0]
		parent['children'].add(child['name'])

for child in sorted(map(lambda x: x['name'] + ' : ' + str(len(findChildren(x)) + 1), data)):
	print(child)
