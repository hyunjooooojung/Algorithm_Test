# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N = int(input())
scores = list(map(int, input().split()))
scores_dict = {}

for idx, score in enumerate(scores):
	scores_dict[idx+1] = score

sorted_scores_dict = sorted(scores_dict.items(), key= lambda x: x[1], reverse=True)

for i in sorted_scores_dict[:3]:
	print(i[0], end=" ")
