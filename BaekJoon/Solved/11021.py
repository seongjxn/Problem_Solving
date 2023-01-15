# BOJ 11021 : A+B - 7
# https://www.acmicpc.net/problem/11021

T = int(input())

for i in range(T) : 
    A, B = map(int, input().split())

    print("Case #%d: %d" %(i + 1, A + B))