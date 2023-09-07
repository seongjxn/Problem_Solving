# BOJ 2439 : 별 찍기 - 2
# https://www.acmicpc.net/problem/2439


import sys
N = int(sys.stdin.readline().rstrip())

for i in range(1, N + 1):
    print(f"{' '*(N-i)}{'*'*i}")