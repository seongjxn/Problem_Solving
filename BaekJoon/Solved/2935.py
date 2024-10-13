# BOJ 2935 : 소음 
# https://www.acmicpc.net/problem/2935


import sys ; input = sys.stdin.readline

A = int(input())
oper = input().rstrip()
B = int(input())

if oper == "*":
    print(A * B)
else :
    print(A + B)