# BOJ 2738 : 행렬 덧셈
# https://www.acmicpc.net/problem/2738


import sys ; input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
Li_1 = [list(map(int, input().rstrip().split())) for _ in range(N)]
Li_2 = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        print(Li_1[i][j] + Li_2[i][j], end=' ')
    print()