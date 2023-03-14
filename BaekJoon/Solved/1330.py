# BOJ 1330 : 두 수 비교하기
# https://www.acmicpc.net/problem/1330


import sys
A, B = map(int, sys.stdin.readline().split())

print('>' if A > B else '<' if A < B else '==')