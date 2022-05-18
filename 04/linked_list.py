from threading import currentThread


class Node:
    next = None
    def __init__(self, value ):
        self.value = value

    def set_next(self, node):
        self.next = node

class Linked_list:
    tail = None
    head = None
    pointer = None


    def set_next_elem_head(self, next_value):
        if self._is_entry_in_list(next_value):
            print("Das Element ist schon vorhanden")
            return

        next_node = Node(next_value)
        if not self.tail:
            self.tail = next_node
            self.head = next_node
            return
        self.head.next = next_node
        self.head = next_node

    def set_next_elem(self, after_value, next_value):    
        if self._is_entry_in_list(next_value):
            print("Das Element ist schon vorhanden")
            return

        new_node = Node(next_value)
        # find the correct node to insert after
        node = self._get_current_node(after_value)
        if not node:
            print("Ein element mit dem Wert gibt es nicht")
            return

        prev_next_node = node.next
        node.next = new_node
        new_node.next = prev_next_node

        if self.head == node:
            self.head = new_node

    def get_next_elem(self, value):
        current_node = self._get_current_node(value)
        if not current_node:
            print("Den Wert gibt es nicht")
            return None
        if not current_node.next:
            return None
            print("es gibt kein nächstes element")
        return current_node.next.value
    
    def remove_next_elem(self, value):
        current_node = self._get_current_node(value)
        if not current_node:
            print("das element gibt es nicht")
            return
        if not current_node.next:
            print("nach dem element gibt es kein element")
            return
        if self.head == current_node.next:
            current_node.next = None
            self.head = current_node
            return
        
        current_node.next = current_node.next.next

    
    def set_prev_elem(self, beforeValue, value):
        if self._is_entry_in_list(value):
            print("Das Element ist schon vorhanden")
            return

        new_node = Node(value)

        # check if the current element exists
        current_node = self._get_current_node(beforeValue)
        if not current_node:
            print("das element gibt es nicht")
            return

        if self.tail == current_node:
            new_node.next = self.tail
            self.tail = new_node
            return

        prev_node = self._get_previous_node(beforeValue)
        
        prev_next_node = prev_node.next
        new_node.next = prev_next_node
        prev_node.next = new_node


    def get_prev_elem(self, value):
        previous_node = self._get_previous_node(value)

        if not previous_node:
            print("das element gibt es nicht")
            return None

        return previous_node.value

    def remove_prev_elem(self, value):
        prev_node = self._get_previous_node(value)

        if not prev_node:
            print("Dieses Element gibt es nicht")
            return

        prev_prev_node = self._get_previous_node(prev_node.value)

        if not prev_prev_node:
            self.tail = prev_node.next
            return
        if prev_node == self.head:
            self.head = prev_prev_node

        prev_prev_node.next = prev_node.next
        prev_node.next = None





    def _get_previous_node(self, value):
        node = self.tail
        while node.next:
            if (node.next.value == value):
                return node
            node  = node.next
        return None

    def _get_current_node(self, value):
        node = self.tail
        while node != None:
            if node.value == value:
                return node
            node = node.next
        return None

    def _is_entry_in_list(self, value):
        if self._get_current_node(value) == None:
            return False
        return True


    def print_all_elements(self):
        counter = 1
        node = self.tail
        while node:
            print(f"{counter}. {node.value}")
            node = node.next
            counter += 1
        print("-" * 20)

    def remove_element(self, value):
        if not self._get_current_node(value):
            print("das element existiert nicht")
            return
        prev_elem = self.get_prev_elem(value)
        if prev_elem:
            return self.remove_next_elem(value)
        
        next_elem = self.get_next_elem(value)
        if next_elem:
            return self.remove_prev_elem(value)

        self.tail = None
        self.head = None

    def insert_element(self, value):
        if type(value) != str:
            print("nur strings sind erlaubt")
            return

        node = self.tail
        while node:
            if (node.value > value):
                self.set_prev_elem(node.value, value)
                return
            node = node.next
        self.set_next_elem_head(value)


       

l = Linked_list()

def print_user_options():
    print("Bitte suchen sie sich eine Aktion aus")
    print("N: neue Liste anlegen")
    print("Z: liste zeigen")
    print("E: element einfügen")
    print("S: element suchen und vorgänger und nochfolger anzeigen")
    print("L: element löschen")
    print("M: element modifizieren" )
    print("*" * 20)
    print("\n")

l = Linked_list()
while True:
    print_user_options()

    eingabe = input().upper()

    if eingabe == "N":
        l = Linked_list()
        print("Neue liste wurde angelegt")

    if eingabe == "Z":
        l.print_all_elements()

    if eingabe == "E":
        element = input("Bitte geben sie ein Element ein, das eingefügt werden soll\n")
        l.insert_element(element)


    if eingabe == "S":
        element = input("Bitte geben sie ein Element ein, das gesucht werden soll \n")
        prev_elem = l.get_prev_elem(element)
        next_elem = l.get_next_elem(element)
        print(f"previous element {prev_elem}, next element {next_elem}")

    if eingabe == "L":
        element = input("Bitte geben sie ein Element ein, das gelöscht werden soll\n")
        l.remove_element(element)

    if eingabe == "M":
        element_mod = input("Bitte geben sie ein element ein, das sie modifizieren wollen\n")
        element_new = input("Bitte geben sie die Änderung ein\n")

        next_elem = l.get_next_elem(element_mod)

        if not next_elem:
            print("das element gibt es nicht, sie können es nicht ändern\n")
        l.remove_prev_elem(next_elem)
        l.insert_element(element_new)


    print("*" * 20)


