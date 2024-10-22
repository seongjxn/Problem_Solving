# BOJ 10828 : 스택
# https://www.acmicpc.net/problem/10828


import sys ; input = sys.stdin.readline

STACK = []

for _ in range(int(input().rstrip())) :
    oper = input().rstrip()
    
    if oper.startswith('push') :
        STACK.append(int(oper.split()[-1]))
    elif oper.startswith('pop') :
        try: print(STACK.pop(-1))
        except: print(-1)
    elif oper.startswith('size') :
        print(len(STACK))
    elif oper.startswith('empty') :
        if STACK : print(0)
        else : print(1)
    elif oper.startswith('top') :
        if STACK : print(STACK[-1])
        else : print(-1)
