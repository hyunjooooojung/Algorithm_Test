# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from itertools import combinations

N = int(input())

coin = 0

for i in [40, 20, 10, 5, 1]:
	if N // i != 0:
		coin += N // i
		N %= i

print(coin)