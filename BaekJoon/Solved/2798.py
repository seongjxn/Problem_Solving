# BOJ 2798 : 블랙잭
# https://www.acmicpc.net/problem/2798


import sys ; input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Li = list(map(int, input().rstrip().split()))

result = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = Li[i] + Li[j] + Li[k]

            if result < total <= M: result = total

print(result)