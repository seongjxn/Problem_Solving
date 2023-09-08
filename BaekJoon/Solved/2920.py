# BOJ 2920 : 음계
# https://www.acmicpc.net/problem/2920


import sys ; input = sys.stdin.readline

Li = list(map(int, input().rstrip().split()))

if   Li == sorted(Li) :               print("ascending")
elif Li == sorted(Li, reverse=True) : print("descending")
else :                                print("mixed")