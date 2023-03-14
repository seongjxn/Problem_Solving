# BOJ 10807 : 개수 세기
# https://www.acmicpc.net/problem/10807


import sys
N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

cnt = 0

for i in L:
    if i == v:
        cnt += 1

print(cnt)