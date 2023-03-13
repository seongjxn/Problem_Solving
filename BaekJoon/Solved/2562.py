list = []
max = [0, 0]
for i in range(9) :
    list.append(int(input()))

for i in range(9) :
    if (list[i] >= max[0]) :
        max[0] = list[i]
        max[1] = i + 1

print(max[0])
print(max[1])
