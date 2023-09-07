# BOJ 2480 : 주사위 세개
# https://www.acmicpc.net/problem/2480


import sys
L = list(map(int, sys.stdin.readline().rstrip().split()))

count_dict = {}
for i in L:
    try:    count_dict[i] += 1
    except: count_dict[i] = 1
        
max_count_key = max(count_dict,key=count_dict.get)
max_count_value = count_dict[max_count_key]

if   max_count_value == 3: price = 10000 + max_count_key * 1000
elif max_count_value == 2: price = 1000  + max_count_key * 100
elif max_count_value == 1: price = max(L) * 100

print(price)