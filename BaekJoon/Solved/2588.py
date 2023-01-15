# BOJ 2588 : 곱셈
# https://www.acmicpc.net/problem/2588

n = int(input())
m = int(input())

print(n * (m % 10))
print(n * ((m // 10) % 10))
print(n * ((m // 100) % 10))
print(n * m)