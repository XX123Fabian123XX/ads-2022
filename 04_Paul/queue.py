
class Queue:
    internalArr: list
    def __init__(self):
        self.internalArr = []

    def enqueue(self, s: str):
        self.internalArr.append(s)

    def dequeue(self) -> str:
        # Simple implementation
        return self.internalArr.pop(0)
        # Complex
        # retVal = self.internalArr[0]
        # self.internalArr = self.internalArr[1:]
        # return retVal

    def first(self) -> str:
        return self.internalArr[0]

    def isempty(self) -> bool:
        return len(self.internalArr) == 0

    def __str__(self) -> str:
        length = len(self.internalArr)
        retVal = "Queue contents ["+str(length)+"]: \n"
        for i in range(0, length):
            retVal += "\t"+str(i+1)+": \""+self.internalArr[i]+"\"\n"
        return retVal


newQueue = Queue()

command = ""    
print("""
    Z = Queue zeigen
    e = enqueue element
    d = dequeue element
    f = first-Element zeigen
    i = "True" wenn leer

    q = Beenden
    """)
    
while command != "q":
    command = input("> ")
    if command == "Z":
        print(newQueue)
    elif command == "e":
        val = input("Eingabewert: ")
        newQueue.enqueue(val)
    elif command == "d":
        print(newQueue.dequeue())
    elif command == "f":
        print(newQueue.first())
    elif command == "i":
        print(newQueue.isempty())
