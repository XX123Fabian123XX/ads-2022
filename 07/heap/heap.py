import math

class Heap:
    heap:list

    ROOT_NODE: int = 1

    def __init__(self):
        self.heap = [0] # Init first element
        pass

    def fromArray(self, arr: list):
        self.heap[1:] = arr
        self.orderHeap()

    def insert(self, value: float):
        self.heap.append(value)
        self.orderHeap()

    def remove(self, pos:int):
        self.swap(pos, len(self.heap)-1)
        self.heap.pop(len(self.heap)-1)
        self.orderHeap()

    def sort(self) -> list:
        sortHeap = Heap()
        sortHeap.heap = self.heap.copy()
        for lastElement in range(len(sortHeap.heap)-1, self.ROOT_NODE-1, -1):
            sortHeap.swap(lastElement, sortHeap.ROOT_NODE)
            sortHeap.orderNode(sortHeap.ROOT_NODE, lastElement)
        return sortHeap.heap[::-1][:-1]

    def orderHeap(self):
        for i in range(self.getLeaves(), self.ROOT_NODE-1, -1):
            self.orderNode(i, len(self.heap))

    def orderNode(self, pos:int, length:int):
        if self.isLeaf(pos):
            return

        if(self.compareToLeftChild(pos, length)):
            self.swap(pos, self.getLeftChildPos(pos))
            self.orderNode(self.getLeftChildPos(pos), length)
        if(self.compareToRightChild(pos, length)):
            self.swap(pos, self.getRightChildPos(pos))
            self.orderNode(self.getRightChildPos(pos), length)

    def compareToLeftChild(self, pos:int, length:int) -> bool:
        if self.getLeftChildPos(pos) >= length:
            return False
        else:
            return self.heap[pos] > self.heap[self.getLeftChildPos(pos)]
    
    def compareToRightChild(self, pos:int, length:int) -> bool:
        if self.getRightChildPos(pos) >= length:
            return False
        else:
            return self.heap[pos] > self.heap[self.getRightChildPos(pos)]

    def getRightChildPos(self, pos: int)-> int:
        return 2*pos

    def getLeftChildPos(self, pos: int)-> int:
        return (2*pos) +1

    def getParentPos(self, pos: int)-> int:
        return max(math.floor(pos/2),1)

    def getLeaves(self)-> int:
        return math.ceil(len(self.heap)/2)

    def isLeaf(self, pos:int) -> bool:
        return pos > self.getLeaves()

    def swap(self, pos1:int, pos2:int):
        temp = self.heap[pos1]
        self.heap[pos1] = self.heap[pos2]
        self.heap[pos2] = temp

    def printHeap(self):
        print(self.heap[1:])

def einlesen() -> list:
    retVal = []
    with open("data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            retVal.append(float(line))
    return retVal

heapObj = Heap()

heapObj.fromArray(einlesen())

command = ""    
print("""
    e = Einfügen eins Elements in den Heap
    l = Löschen des kleinsten Elements aus dem Heap
    s = sortiertes Ausgeben des Heaps (= HeapSort durchführen)
    a = Ausgeben des Arrays
    n = erneutes Einlesen der Datei

    q = Beenden
    """)
    
while command != "q":
    command = input("> ")
    if command == "a":
        heapObj.printHeap()
    elif command == "e":
        val = input("Eingabewert: ")
        try:
            heapObj.insert(float(val))
            print("\""+str(val)+"\" wurde eingefügt!")
        except:
            print("\""+str(val)+"\" konnte nicht hinzugefügt werden. Bitte probiere es noch einmal mit einer Fließkommazahl (punkt als trenner!)")
    elif command == "l":
        try:
            heapObj.remove(heapObj.ROOT_NODE)
            print("Wurzel wurde entfernt")
        except:
            print("Die Wurzel konnte nicht entfernt werden!")
    elif command == "n":
        try:
            heapObj.fromArray(einlesen())
            print("Daten erneut aus datei eingelesen!")
        except:
            print("Datei konnte nicht gelesen werden!")
    elif command == "s":
        try:
            print(heapObj.sort())
            print("Heap wurde sortiert!")
        except:
            print("Heap konnte nicht sortiert werden!")