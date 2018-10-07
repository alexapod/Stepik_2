"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:

this is a text
"this' !is. ?n1ce,
Sample Output:

htis si a etxt
"htis' !si. ?1nce,
"""

import sys
import re

for line in sys.stdin:
	line = line.rstrip()
	list = re.split(r'\W+', line)

	if len(list) is not None:
		for word in list:
			if len(word) >= 2:
				rWord = word[1] + word[0]
				if len(list) >= 3:
					rWord += word[2:]
				pattern = r'\b' + word + r'\b'
				line = re.sub(pattern, rWord, line)
	print(line)
