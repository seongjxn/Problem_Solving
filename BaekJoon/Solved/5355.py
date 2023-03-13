# BOJ 5355 : 화성 수학
# https://www.acmicpc.net/problem/5355


import sys
T = int(sys.stdin.readline().rstrip())


def calc(a, b):
    if b == '@':
        a *= 3
    if b == '%':
        a += 5.0
    if b == '#':
        a -= 7.0

    return a


for i in range(T):
    L = sys.stdin.readline().split()
    L[0] = float(L[0])
    for j in range(1, len(L)):
        L[0] = calc(L[0], L[j])
    print("%.2f" %L[0])
