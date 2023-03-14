# BOJ 9086 : 문자열
# https://www.acmicpc.net/problem/9086


import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    S = sys.stdin.readline().rstrip()

    print(S[0] + S[-1])