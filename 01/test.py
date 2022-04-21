import math
a = 2
b = 14
count = 0
ins = 0
for i in range(a, b):
    for j in range(2, 4):
        ins += 1
        print(i, j)
        if j * i % 2 == 0:
            print(j, i)
            count += 1

print(ins)
print(count)
print(2 * (b-a) - math.floor((b-a) / 2))