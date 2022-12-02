N, M = map(int, input().split())
L = [0] * M
R = [0] * M
A = [0] * M
r = [0] * M
result = 0

for i in range(M) :
    L[i], R[i], A[i] = map(int, input().split())

    if (A[i] <= N) and (A[i] <= (R[i] - L[i])) :
        r[i] = 1

for i in r : 
    if (i == 1) :
        result = 1

print(result)