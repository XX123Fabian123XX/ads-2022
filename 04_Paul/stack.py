
class Stack:
    internalArr: list
    def __init__(self):
        self.internalArr = []

    def push(self, s: str):
        self.internalArr.append(s)

    def pop(self) -> str:
        # Simple implementation
        return self.internalArr.pop(-1)
        # Complex
        # retVal = self.internalArr[-1]
        # self.internalArr = self.internalArr[0:-1]
        # return retVal

    def top(self) -> str:
        return self.internalArr[-1]

    def isempty(self) -> bool:
        return len(self.internalArr) == 0

    def __str__(self) -> str:
        length = len(self.internalArr)
        retVal = "Stack contents ["+str(length)+"]: \n"
        for i in range(length-1, -1, -1):
            retVal += "\t"+str(length-i)+": \""+self.internalArr[i]+"\"\n"
        return retVal


newStack = Stack()

command = ""    
print("""
    Z = Stack zeigen
    u = push element
    o = pop element
    t = top-Element zeigen
    i = "True" wenn leer

    q = Beenden
    """)
    
while command != "q":
    command = input("> ")
    if command == "Z":
        print(newStack)
    elif command == "u":
        val = input("Eingabewert: ")
        newStack.push(val)
        print("Pushed!")
    elif command == "o":
        print(newStack.pop())
    elif command == "t":
        print(newStack.top())
    elif command == "i":
        print(newStack.isempty())
