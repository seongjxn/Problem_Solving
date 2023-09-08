# BOJ 2577 : 숫자의 개수
# https://www.acmicpc.net/problem/2577


import sys ; input = sys.stdin.readline
num = int(input().rstrip())
num *= int(input().rstrip())
num *= int(input().rstrip())

for i in range(10) :
    print(str(num).count(str(i)))