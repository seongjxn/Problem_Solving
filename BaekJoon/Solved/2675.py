# BOJ ** : **
# https://www.acmicpc.net/problem/**


import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split()
    R = int(R)
    res = ""

    for i in range(len(S)):
        res += S[i] * R

    print(res)