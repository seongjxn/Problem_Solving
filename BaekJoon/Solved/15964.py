# BOJ 15964 : 이상한 기호
# https://www.acmicpc.net/problem/15964


import sys
A, B = map(int, sys.stdin.readline().rstrip().split())

print((A + B) * (A - B))