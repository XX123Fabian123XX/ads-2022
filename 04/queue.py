

class Queue:

    def __init__(self, length):
        self.length = length
        self.front_index = 0
        self.back_index = None
        self.queue_list = [None for x in range(length)]        


    def enqueue(self, element):
        if self.front_index == self.length and self.back_index == 0 :
            print("Die queue ist voll")
            return
        
        if self.front_index == self.length:
            self.front_index = 0
        if self.queue_list[self.front_index] != None:
            print("Die queue ist voll")
            return
        
        self.queue_list[self.front_index] = element
        self.front_index = self.front_index + 1

        if (self.back_index == None):
            self.back_index = self.front_index - 1

    def dequeue(self):
        if self.back_index == None:
            print("die liste ist leer")
            return
        
        self.back_index = self.back_index + 1

        if self.back_index == self.length:
            self.back_index = 0


        value = self.queue_list[self.back_index - 1]
        self.queue_list[self.back_index - 1] = None

        if self.back_index == self.front_index:
            self.back_index = None


        return value

    def is_empty(self):
        return self.back_index == None

    def print_list(self):
        for key, value in enumerate(self.queue_list):
            print(f"{key}. {value}")

        self.print_indexes()

    def print_indexes(self):
        print(f"front: {self.front_index}, back {self.back_index}")

q = Queue(5)




while True:
    print("a: enqueu")
    print("b: dequeue")
    print("c: is empty")
    print("d: ausgabe")
    print("---------------------------")
    eingabe = input()

    if eingabe == 'a':
        element = input("Bitte ein Element eingeben \n")
        q.enqueue(element)

    if eingabe == 'b':
        print(q.dequeue())
    
    if eingabe == 'c':
        print(q.is_empty())

    if eingabe == 'd':
        q.print_list()

