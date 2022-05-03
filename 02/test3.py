from sympy import maximum


def rechtesRandMax(A, li, re):
    zwischensumme = 0
    maximum = 0
    for i in range(re,li, -1):
        zwischensumme += A[i]
        maximum = max(maximum,zwischensumme)
    return maximum

def linkesRandMax(A, li ,re):
    zwischensumme = 0
    maximum = 0
    for i in range(li, re):
        zwischensumme += A[i]
        maximum = max(maximum, zwischensumme)
    return maximum
counter = 0

def maxTeilsumme(A, links, rechts):
    global counter
    counter += 1
    if links == rechts:
        return max(A[links],0)
    m = (links + rechts) // 2

    maxrl = rechtesRandMax(A, links, m)
    maxlr = linkesRandMax(A, m+1, rechts)

    return (max(maxTeilsumme(A, links, m), maxTeilsumme(A, m+1, rechts), maxlr + maxrl))

arr = [1,2,3,4,5,6,123,1,31,23,12,1,12,31231231,123123,1,23,12,312,37,8,9,10]
maxTeilsumme(arr,0, len(arr) - 1)
print(counter)
print(len(arr) * 2 - 1)