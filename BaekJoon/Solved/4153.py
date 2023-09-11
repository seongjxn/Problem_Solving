# BOJ 4153 : 직각삼각형
# https://www.acmicpc.net/problem/4153


import sys ; input = sys.stdin.readline

while True:
    nums = list(map(int, input().rstrip().split()))

    if not sum(nums): break

    maxn = max(nums)
    nums.remove(maxn)

    print('right' if nums[0] ** 2 + nums[1] ** 2 == maxn ** 2 else 'wrong')