"""
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
Sample Input:

zabcz
zzz
zzxzz
zz
zxz
zzxzxxz
Sample Output:

zabcz
zzxzz
"""

import sys
import re

pattern = 'z\w\w\wz'
for line in sys.stdin:
	line = line.rstrip()
	a = re.findall(pattern, line)
	if len(a) != 0:
		print(line)
