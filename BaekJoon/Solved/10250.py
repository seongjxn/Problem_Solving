# BOJ 10250 : ACM 호텔
# https://www.acmicpc.net/problem/10250


import sys ; input = sys.stdin.readline

for _ in range(int(input().rstrip())) :
    H, W, N = map(int, input().rstrip().split())
    
    height = N % H
    width  = N // H + 1

    if N % H == 0 :
        height = H
        width  = N // H

    print(height * 100 + width)