import sys

grade_dict = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
sum_all = 0
sum_score = 0

for _ in range(20):
    subject, score, grade = map(str, sys.stdin.readline().split())
    if grade != "P":
        sum_all += (float(score) * grade_dict[grade])
        sum_score += float(score)

print(f"{(sum_all / sum_score):.6f}")