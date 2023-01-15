# BOJ 1463 : 1로 만들기
# https://www.acmicpc.net/problem/1463

"""
N = int(input())
cnt = 0

while (N > 1):
    if (N - 1) % 3 == 0 :
        N -= 1
        N /= 3
        cnt += 2
    if N % 3 == 0 :
        N /= 3
        cnt += 1
    
    if N % 2 == 0 :
        N /= 2
        cnt += 1

print(cnt)
"""

N = int(input())
DP = [0 for _ in range(N + 1)]

for i in range(2, N + 1) :
    DP[i] = DP[i - 1] + 1

    if i % 2 == 0 :
        DP[i] = min(DP[i], DP[i // 2] + 1)

    if i % 3 == 0 :
        DP[i] = min(DP[i], DP[i // 3] + 1)
        
print(DP[N])