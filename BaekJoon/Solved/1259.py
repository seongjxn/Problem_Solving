# BOJ 1259 : 팰린드롬수
# https://www.acmicpc.net/problem/1259

while ((case := input()) != "0") :   
    print("yes") if case == case[::-1] else print("no")