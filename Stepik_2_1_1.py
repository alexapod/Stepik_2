"""
1.1 Введение

Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.
Выведите одно число – сумму данных n чисел.
Примечание:
﻿Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код
n = int(input())

Sample Input 1:
2
2
3
Sample Output 1:
5
"""

c = 0
for i in range(int(input())):
	c += int(input())
print(c)
