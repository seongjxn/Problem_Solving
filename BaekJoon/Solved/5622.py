# BOJ 5622 : 다이얼
# https://www.acmicpc.net/problem/5622


import sys ; input = sys.stdin.readline

def solution(word) :
    Li = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    result = 0

    for i in word:
        for j in Li:
            if i in j:
                result += Li.index(j) + 3
                break

    return result


if __name__ == '__main__' :
    print(solution(input().rstrip()))
