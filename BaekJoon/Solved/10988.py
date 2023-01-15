# BOJ 10988 : 팰린드롬인지 확인하기
# https://www.acmicpc.net/problem/10988

input = input()

print(1) if input == input[::-1] else print(0)