# BOJ 2530 : 인공지능 시계
# https://www.acmicpc.net/problem/2530


A, B, C = map(int, input().split())
D = int(input())

C += D
while (C >= 60) :
    B += C // 60
    C %= 60

while (B >= 60) :
    A += B // 60
    B %= 60

if A >= 24: A %= 24

print(A, B, C)
