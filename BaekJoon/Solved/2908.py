# BOJ 2908 : 상수 
# https://www.acmicpc.net/problem/2908


import sys ; input = sys.stdin.readline

A, B = map(str, input().rstrip().split())
A, B = A[::-1], B[::-1]

print(A if int(A) > int(B) else B)