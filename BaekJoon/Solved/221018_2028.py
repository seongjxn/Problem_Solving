T = int(input())
N = []
for i in range(T) :
    N.append(int(input()))

for i in range(T) :
    if ((N[i] * N[i]) % 10 == N[i]) :
        print('YES')
    elif ((N[i] * N[i]) % 100 == N[i]) :
        print('YES')
    elif ((N[i] * N[i]) % 1000 == N[i]) :
        print('YES')
    elif ((N[i] * N[i]) % 10000 == N[i]) :
        print('YES')
    else :
        print('NO')