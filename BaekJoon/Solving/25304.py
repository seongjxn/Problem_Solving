# BOJ 25304 : 영수증
# https://www.acmicpc.net/problem/25304


import sys
X = int(sys.stdin.readline().rstrip())

for _ in range(int(sys.stdin.readline().rstrip())) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    X -= a * b

print("Yes" if not X else "No")