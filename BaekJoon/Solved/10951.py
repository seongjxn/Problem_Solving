# BOJ 10951 : A+B - 4
# https://www.acmicpc.net/problem/10951


import sys
while True:
    tmp = sys.stdin.readline()

    if tmp == "\n":
        break

    A, B = tmp.split()
    print(A + B)
