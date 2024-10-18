# BOJ 1546 : 평균
# https://www.acmicpc.net/problem/1546


import sys ; input = sys.stdin.readline

N = int(input().rstrip())
score = list(map(int, input().rstrip().split()))
M = max(score)

sum = 0
for i in score :
    new_score = i / M * 100
    sum += new_score

print(sum / N)