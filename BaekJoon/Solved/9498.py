# BOJ 9498 : 시험 성적
# https://www.acmicpc.net/problem/9498


import sys
a = int(sys.stdin.readline().rstrip())

print('A' if ((a >= 90) and (a <= 100)) else 'B' if (a >= 80) else 'C' if (a >= 70) else 'D' if (a >= 60) else 'F')