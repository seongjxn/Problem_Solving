# BOJ 2475 : 검증수
# https://www.acmicpc.net/problem/2475


import sys
L = list(map(int, sys.stdin.readline().split()))

for i in range(len(L)):
    L[i] *= L[i]

print(sum(L) % 10)