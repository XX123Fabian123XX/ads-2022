i = 4
n = 16
count = 0
# res = ((n - (n % 3)) - (i + 3 - (i % 3))) / 3 + 1

res = ((n - (n % 3)) - (i)) / 3 + 1
print(res)
while i <= n:
    if i % 3 == 0:
        count += 1
    i+=1
print(count)