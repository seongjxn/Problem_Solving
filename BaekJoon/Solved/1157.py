# BOJ 1157 : 단어 공부
# https://www.acmicpc.net/problem/1157


import sys ; input = sys.stdin.readline
from collections import Counter

count = Counter(input().rstrip().upper())

if len(Li := [k for k,v in count.items() if max(count.values()) == v]) > 1 :
    print('?')
else:
    print(Li[0])