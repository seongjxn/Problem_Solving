# BOJ 8958 : OX퀴즈
# https://www.acmicpc.net/problem/8958


import sys ; input = sys.stdin.readline

def solution(Li) :
    res = [0]

    for i in range(len(Li)):
        if Li[i] == 'O' : res.append(res[i] + 1)
        else :            res.append(0)

    return sum(res)

if __name__ == '__main__' :
    for _ in range(int(input().rstrip())) :
        print(solution(list(input().rstrip())))