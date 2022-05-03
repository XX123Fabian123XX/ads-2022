arr = [1,2,89,3,-94,4]
maxiumZahl = 0
zwischensumme = 0
von = bis = 0

for i in range(len(arr)):

    zwischensumme = max(0, zwischensumme + arr[i])
    if (zwischensumme == 0):
        von = i+1

    maxiumZahl = max(maxiumZahl, zwischensumme)

    if (zwischensumme == maxiumZahl):
        bis = i

print(maxiumZahl)
print(von, bis)