# BOJ 10809 : 알파벳 찾기
# https://www.acmicpc.net/problem/10809


import sys ; input = sys.stdin.readline

word = input().rstrip()

for alpha in 'abcdefghijklmnopqrstuvwxyz':
    print(word.index(alpha) if alpha in word else '-1', end=' ')