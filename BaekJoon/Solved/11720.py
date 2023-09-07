# BOJ 11720 : 숫자의 합
# https://www.acmicpc.net/problem/11720


import sys
N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip()))

print(sum(L))