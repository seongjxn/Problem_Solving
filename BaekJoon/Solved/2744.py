# BOJ 2744 : 대소문자 바꾸기
# https://www.acmicpc.net/problem/2744


import sys
word = str(sys.stdin.readline().rstrip())
result = ""

for i in range(len(word)):
    if word[i].isupper():
        result += word[i].lower()
    else :
        result += word[i].upper()

print(result)