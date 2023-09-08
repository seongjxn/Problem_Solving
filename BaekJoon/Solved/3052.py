# BOJ 3052 : 나머지
# https://www.acmicpc.net/problem/3052


import sys ; input = sys.stdin.readline

nums = [int(input().rstrip()) for _ in range(10)]
Li = []

for num in nums :
    if (rem := num % 42) not in Li :
        Li.append(rem)

print(len(Li))