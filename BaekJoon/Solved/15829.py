# BOJ 15829 : Hashing
# https://www.acmicpc.net/problem/15829


import sys ; input = sys.stdin.readline

def solution(num, Li) :
    r = 31
    M = 1234567891

    for i in range(num) :
        Li[i] = (ord(Li[i]) - 96) * (r ** i)
    return sum(Li) % M

if __name__ == '__main__' :
    n = int(input().rstrip())
    Li = list(input().rstrip())
    
    print(solution(n, Li))
