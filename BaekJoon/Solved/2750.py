N = int(input())
list = []

for _ in range(N) :
    list.append(int(input()))

for _ in range(N):
    print(min(list))
    list.remove(min(list))    