class Stack:
    stackElements = []
    def push(self, element):
        self.stackElements.append(element)

    def pop(self):
        if self.is_empty():
            return ""
        return self.stackElements.pop()

    def is_empty(self):
        return len(self.stackElements) == 0
    
    def top(self):
        if self.is_empty():
            return ""
        return self.stackElements[-1]

    def print_elements(self):
        for key, element in enumerate(self.stackElements):
            print(f"{key}. {element}")


s = Stack()

def print_options():
    print("a: push")
    print("b: pop")
    print("c: isEmpty")
    print("d: top")
    print("e: print_elements")
    print("---------------------------")

while True:
    print_options()
    eingabe = input()

    if eingabe == "a":
        element = input("Bitte geben sie einen String ein\n")
        s.push(element)

    if eingabe == "b":
        print(s.pop())

    if eingabe == "c":
        print(s.is_empty())

    if eingabe == "d":
        print(s.top())

    if eingabe == "e":
        s.print_elements()





