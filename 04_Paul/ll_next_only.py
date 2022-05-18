
class LinkedListElement:
    value: str
    next: LinkedListElement
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self) -> str:
        retVal = " \""+self.value+"\" "
        if self.next != None:
            retVal += str(self.next)
        return retVal

class LinkedList:
    head: LinkedListElement
    current: LinkedListElement

    def __init__(self):
        self.head = None
        self.current = None

    def setNextElem(self, value: str):
        if self.current == None:
            if self.head == None:
                self.head = LinkedListElement(value)
                self.current = self.head.next
            else:
                self.current = LinkedListElement(value)
        else:
            nextAfter = self.current.next
            self.current.next = LinkedListElement(value)
            self.current.next.next = nextAfter

    def getNextElem(self) -> str:
        return self.current.next

    def removeNextElem(self):
        if(self.current.next):
            self.current.next = self.current.next.next

    def getIdxOfCurrentElement(self) -> int:
        retVal = 0
        tempVal = self.head
        while(tempVal.next != self.current):
            retVal+=1
        return retVal
    
    def getElementAtIdx(self, idx:int):
        tempIdx = 0
        tempVal = self.head
        while tempVal != None and tempIdx < idx:
            tempIdx+=1
            tempVal = tempVal.next
        return tempVal

    def getPrevElem(self):
        idx = self.getIdxOfCurrentElement()
        return self.getElementAtIdx(idx-1)

    def setPrevElem(self, value: str):
        idx = self.getIdxOfCurrentElement()
        if(idx >= 0):
            self.getElementAtIdx(idx-1).value = value
        else:
            # replace head
            tempHead = self.head
            self.head = LinkedListElement(value)
            self.head.next = tempHead

    def removePrevElem(self):
        idx = self.getIdxOfCurrentElement()
        if(idx == 1):
            self.head = self.head.next
        elif(idx > 1):
            self.getElementAtIdx(idx-2).next = self.current




newLinkedList: LinkedList

command = ""    
print("""
    N = neue Liste anlegen
    L = Liste löschen
    Z = Liste zeigen
    e = Element hinter einem anderen einfügen (bzw. in die leere Liste schreiben)
    s = Element suchen und Vorgänger und Nachfolger anzeigen
    l = Element löschen
    m = Element modifizieren

    q = Beenden
    """)
    
while command != "q":
    command = input("> ")

    if command == "N":
        val = input("Startwert: ")
        newLinkedList = LinkedList()

    elif command == "L":
        while newLinkedList != None:
            length = 0
            tempLL = newLinkedList
            while tempLL != None:
                length += 1
                tempLL = tempLL.next

            if length == 0:
                newLinkedList = None

            else: 
                # Remove previous element!
                length -= 1
                tempLL = newLinkedList
                while tempLL != None:
                    length -= 1
                    if length == 0:
                        tempLL.next = None
                    tempLL = tempLL.next


    elif command == "Z":
        print(newLinkedList)

    elif command == "e":
        val = input("Eingabewert: ")
        newLinkedList.enLinkedList(val)
    elif command == "s":
        print(newLinkedList.deLinkedList())
    elif command == "l":
        print(newLinkedList.first())
    elif command == "m":
        print(newLinkedList.isempty())
