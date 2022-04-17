#Aufgabe
import sys
import time

## ermittelt informationen über die größste Teilsumme
## die Zahlen müssen in einer Datei in der ersten Zeile stehen und mit Kommas (ohne Leerzeichen getrennt werden)
def maxTeilsumme():
    running = True
    while running:
        dateiname = input("Bitte geben sie den Dateinamen ein ")
        arr = []
        try:
            with open(dateiname) as k:
                ## fehlerbehandlung fehlt, wenn es kein int ist
                for num in k.readline().split(","):
                    arr.append(int(num))
                
                running = False
        except:
            print("Sie haben keinen gültigen dateinamen eingegeben")

        laenge = len(arr)

        # smallest int value
        # https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
        maxsumme = - sys.maxsize * 2 + 1 
        von, bis = 0, 0
        anzahlAdditionen = 0
        starttime = time.time()
        for i in range(0, laenge):
            for j in range(i, laenge):
                summe = 0
                for k in range(i, j + 1):
                    summe += arr[k]
                    anzahlAdditionen += 1
                if summe > maxsumme:
                    maxsumme = summe
                    von = i
                    bis = j
        print(f"zeit {time.time() - starttime} sekunden")      
        print(f"max. Teilsumme {maxsumme}") 
        print(f"erster Index {von}")
        print(f"zweiter index {bis}")
        print(f"Anzahl Additionen {anzahlAdditionen}")       

maxTeilsumme()