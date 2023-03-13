# BOJ 2914 : 저작권
# https://www.acmicpc.net/problem/2914


import sys
A, I = map(int, sys.stdin.readline().split())

print(A * (I - 1) + 1)