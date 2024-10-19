# BOJ 2609 : 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609


import sys ; input = sys.stdin.readline

A, B = map(int, input().rstrip().split(" "))

def func(A, B) -> int:
    if N:=A % B :
        return func(B, N)
    return B

GCD = func(A, B)
LCM = int(A * B / GCD)

print(GCD)
print(LCM)
