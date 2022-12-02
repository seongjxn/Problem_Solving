
N, M = map(int, input().split())
A, B, C = map(int, input().split())
X = []
Y = []

for i in range(N) :
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count = 0
H = 0
maxH = 0

while (count < M) :
    N -= 1

    if ((C + X[count]) >= A) :
        C = A
        break
    else :
        C += X[count]
        H += Y[count]
    
    C -= B

    count += 1

print(maxH)