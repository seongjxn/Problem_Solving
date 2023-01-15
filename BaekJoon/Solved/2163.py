# BOJ 2163 : 초콜릿 자르기
# https://www.acmicpc.net/problem/2163

N, M = map(int, input().split())

print((N - 1) + (N * (M - 1)))