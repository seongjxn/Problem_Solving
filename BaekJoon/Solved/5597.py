# BOJ 5597 : 과제 안 내신 분..?
# https://www.acmicpc.net/problem/5597

list = [i for i in range(1, 31)]

for i in range(28) :
    n = int(input())

    list.remove(n)

print(list[0])
print(list[1])