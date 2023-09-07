# BOJ 10818 : 최소, 최대
# https://www.acmicpc.net/problem/10818


import sys
N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))

print(f"{min(L)} {max(L)}")