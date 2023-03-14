# BOJ 15552 : 빠른 A+B
# https://www.acmicpc.net/problem/15552


import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())

    print(A + B)