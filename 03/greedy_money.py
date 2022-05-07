"""
Datenstruktur   Klasse für Coin, da leichte Anpassung / Nutzung der Parameter (used und number in Kombination)
                Klasse für Game, damit nicht überall Parameter übergeben (arrCoins)

Rest = 200
Vorhanden   Greedy = Optimal
(50,3)      (50,3)
(20,5)      (20,2)
(10,20)     (10,1)

Rest = 18
Vorhanden   Greedy  = Optimal
(8,3)       (8,2)
(4,5)       (4,0)
(2,20)      (2,1)

Rest = 34
Vorhanden   Greedy  Optimal
(26,5)      (26,1)  (26,0)
(16,3)      (16,0)  (16,2)
(2,100)     (2,4)   (2,1)

Rest = 93
Vorhanden   Greedy  Optimal
(39,2)      (39,2)  (39,0)
(29,4)      (29,0)  (29,3)
(3,20)      (3,5)   (3,2)
"""

INVALID = "Ungültige Eingabe!"

class Till:
    arrCoins = []
    rest = 0

    def __init__(self):
        arr = []
        while True:
            value = input("Bitte geben Sie eine neue verfügbare Münze ein: ")
            if value == "" and len(arr): # no more coins
                break
            try:
                value = int(value)
                available = False
                for i in arr:
                    if i.value == value:
                        print(f"Münzwert {value} bereits vorhanden!")
                        available = True
                if available:
                    continue

                while True:
                    number = input(f"Bitte geben Sie die Anzahl der Münze '{value}' an: ")
                    try:
                        number = int(number)
                        arr.append(Coin(value,number))
                        break
                    except:
                        print(INVALID)
            except:
                print(INVALID)
        
        self.arrCoins = sorted(arr, key=customSort, reverse=True)
    
    def getAmounts(self):
        while True:
            toPayAmount = input("Bitte geben Sie die zu zahlende Summe an: ")
            if toPayAmount == "":
                exit()
            try:
                toPayAmount = int(toPayAmount)
                break
            except:
                print(INVALID)
        while True:
            givenAmount = input("Bitte geben Sie den gegebenen Betrag an: ")
            try:
                givenAmount = int(givenAmount)
                break
            except:
                print(INVALID)
        self.rest = givenAmount - toPayAmount
    
    def change(self):
        for i in self.arrCoins:
            # stop calculating if already solution 
            if self.rest == 0:
                break
            # save also used coin
            while i.number > i.used and self.rest - i.value >= 0:
                i.used += 1
                self.rest -= i.value
        
        # print and prepare for next change request
        if self.rest == 0:
            print(self.arrCoins)
            for i in self.arrCoins:
                i.number -= i.used
                i.used = 0
        else:
            for i in self.arrCoins:
                i.used = 0
            print("Geldwechsel nicht möglich")

class Coin:
    value = 0
    number = 0
    used = 0
    def __init__(self, value, number):
        self.value = value
        self.number = number
    def __str__(self):
        return f"({self.value}, {self.used})"

    def __repr__(self):
        return self.__str__()

""" sort Coins by coin value"""   
def customSort(k):
    return k.value


till = Till()
while True:
    till.getAmounts()
    till.change()
