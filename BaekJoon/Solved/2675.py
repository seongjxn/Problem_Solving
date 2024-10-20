# BOJ 2675 : 문자열 반복
# https://www.acmicpc.net/problem/2675


import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    res = ""

    for i in range(len(S)):
        res += S[i] * R

    print(res)