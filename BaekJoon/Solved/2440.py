# BOJ 2440 : 별 찍기 - 3
# https://www.acmicpc.net/problem/2440


import sys ; input = sys.stdin.readline

N = int(input().rstrip())

for i in range(N, 0, -1) :
    print(f"{'*'*i}")