# BOJ 31403 : A + B - C
# https://www.acmicpc.net/problem/31403


import sys ; input = sys.stdin.readline

A, B, C = [input().strip() for _ in range(3)]

print(eval(A) + eval(B) - eval(C))
print(eval(A + B) - eval(C))