N = int(input()) # 과목 개수
scores = list(map(int, input().split())) # 점수

new_scores = [(scores[i]/ max(scores)) * 100 for i in range(N)]
print(sum(new_scores) / N)