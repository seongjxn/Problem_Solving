# BOJ 2670 : 연속부분최대곱
# https://www.acmicpc.net/problem/2670


import sys ; input = sys.stdin.readline

N = int(input())
list = [float(input()) for _ in range(N)]

for i in range(1, N) :
    if (list[i] < list[i] * list[i - 1]) :
        list[i] *= list[i - 1]

print("{:.3f}".format(max(list)))