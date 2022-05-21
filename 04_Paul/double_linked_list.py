
class Node:
    next = None
    previous = None
    def __init__(self, value ):
        self.value = value



class Linked_list:
    head = None
    tail = None
    pointer = None


    def set_next_elem_tail(self, next_value):
        if self._is_entry_in_list(next_value):
            print("Das Element ist schon vorhanden")
            return

        next_node = Node(next_value)
        if not self.head:
            self.head = next_node
            self.tail = next_node
            return
        self.tail.next = next_node
        next_node.previous =self.tail
        self.tail = next_node

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
        new_node.previous = node
        
        new_node.next = prev_next_node
        prev_next_node.previous = new_node

        if self.tail == node:
            self.tail = new_node

    def get_next_elem(self, value):
        current_node = self._get_current_node(value)
        if not current_node:
            print("Den Wert gibt es nicht")
            return None
        if not current_node.next:
            print("es gibt kein nächstes element")
            return None
        return current_node.next.value
    
    def remove_next_elem(self, value):
        current_node = self._get_current_node(value)
        # Removes current_node.next! -->
        # current_node          .next            .next.next
        #    <------------------------------------- prev
        #    next--------------------------------------> 
        if not current_node:
            print("das element gibt es nicht")
            return
        if not current_node.next:
            print("nach dem element gibt es kein element, das gelöscht werden könnte")
            return
        if self.tail == current_node.next:
            current_node.next = None
            self.tail = current_node
            return
        current_node.next.next.previous = current_node
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

        if self.head == current_node:
            new_node.next = self.head
            current_node.previous = new_node
            self.head = new_node
            return

        prev_node = self._get_previous_node(beforeValue)
        
        prev_node.next.previous = new_node
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.previous = prev_node

    def get_prev_elem(self, value):
        previous_node = self._get_previous_node(value)

        if not previous_node:
            print("das element gibt es nicht")
            return None

        return previous_node.value

    def remove_prev_elem(self, value):
        prev_node = self._get_previous_node(value)
        # Removes prev_node! -->
        # prev_node.prev          prev_node            prev_node.next
        #    <------------------------------------- prev
        #    next--------------------------------------> 

        if not prev_node:
            print("Dieses Element gibt es nicht")
            return

        #prev_prev_node = self._get_previous_node(prev_node.value)

        if not prev_node.previous:
            # Node is head
            self.head = prev_node.next
            return

        if prev_node.next == None:
            # Node is tail
            self.tail = prev_node.previous

        prev_node.previous.next = prev_node.next
        prev_node.previous = prev_node.previous

        # Unneccessary
        prev_node.next = None
        prev_node.previous = None



    def _get_previous_node(self, value):
        node = self.head
        while node.next:
            if (node.next.value == value):
                return node
            node  = node.next
        return None

    def _get_current_node(self, value):
        node = self.head
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
        node = self.head
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
            return self.remove_next_elem(prev_elem)
        
        next_elem = self.get_next_elem(value)
        if next_elem:
            return self.remove_prev_elem(next_elem)

        self.head = None
        self.tail = None

    def insert_element(self, value):
        if type(value) != str:
            print("nur strings sind erlaubt")
            return

        node = self.head
        while node:
            if (node.value > value):
                self.set_prev_elem(node.value, value)
                return
            node = node.next
        self.set_next_elem_tail(value)

    def print_individual_nodes(self):
        current_node = self.head
        while current_node:
            print(f"Wert {current_node.value}")

            if current_node.previous:
                print(f"Vorgänger {current_node.previous.value}")
            if current_node.next:
                print(f"Nachfolger {current_node.next.value}")

            print("*" * 20)
            current_node = current_node.next
       



def print_user_options():
    print("Bitte suchen sie sich eine Aktion aus")
    print("N: neue Liste anlegen")
    print("L: Liste löschen")
    print("Z: liste zeigen")
    print("e: element einfügen")
    print("s: element suchen und vorgänger und nochfolger anzeigen")
    print("l: element löschen")
    print("m: element modifizieren" )
    print("*" * 20)
    print("\n")

l = Linked_list()
while True:
    print_user_options()

    eingabe = input().upper()

    if eingabe == "N":
        l = Linked_list()
        print("Neue liste wurde angelegt")

    if eingabe == "L":
        l = None
        print("Liste wurde gelöscht")

    if eingabe == "Z":
        l.print_all_elements()
        l.print_individual_nodes()

    if eingabe == "e":
        element = input("Bitte geben sie ein Element ein, das eingefügt werden soll\n")
        l.insert_element(element)


    if eingabe == "s":
        element = input("Bitte geben sie ein Element ein, das gesucht werden soll \n")
        prev_elem = l.get_prev_elem(element)
        next_elem = l.get_next_elem(element)
        print(f"previous element {prev_elem}, next element {next_elem}")

    if eingabe == "l":
        element = input("Bitte geben sie ein Element ein, das gelöscht werden soll\n")
        l.remove_element(element)

    if eingabe == "m":
        element_mod = input("Bitte geben sie ein element ein, das sie modifizieren wollen\n")
        element_new = input("Bitte geben sie die Änderung ein\n")

        next_elem = l.get_next_elem(element_mod)

        if not next_elem:
            print("das element gibt es nicht, sie können es nicht ändern\n")
        l.remove_prev_elem(next_elem)
        l.insert_element(element_new)


    print("*" * 20)


