import time

def hash(text):
    """
    Hash function for strings. Adds up the ascii values of each letter 
    and takes mod 53
    """
    sum = 0
    for i in list(text):
        sum = sum + ord(i)
    return sum % 53

def load_words(number_words, hashValue):
    """
    returns an array words with a length number_words with a specific hash
    """
    words = []

    with open("words2.txt", 'r') as k:
        for word in k.readlines():
            newstring = word.replace("\n", "")
            if hash(newstring) == hashValue:
                words.append(newstring)

    if len(words) > number_words:
        return words[:number_words]

    return words


class Hash_table:
    
    table = []

    def __init__(self):
        for i in range(53):
            self.table.append(LinkedList())


    def insert(self, value):
        """ 
        insert a value into the hash table
        """

        hash_value = hash(value)

        if self.is_in_table(value):
            print("ist schon in der tablele")
            return

        self.table[hash_value].insert(value)
    
    def delete(self, value):
        """
        deletes a value out of the hash table, if it exists
        """
        if not self.is_in_table(value):
            print("Das Element gibt es nicht in der tablele")
            return 


        hash_value = hash(value)

        linked_list= self.table[hash_value]

        node = linked_list.head
        
        # check if the linked_list is empty
        if not node:
            print("linked list is empty")
            return

        # check the head
        if node.data == value:
            print("value is at head")
            linked_list.head = node.next
            return 

        while node.next:
            if node.next.data == value:
                if not node.next.next:
                    node.next = None
                    return 

                node.next = node.next.next
                return

            node = node.next


    def is_in_table(self, value):
        hash_value = hash(value)

        linked_list = self.table[hash_value]

        node = linked_list.head

        while node:
            if node.data == value:
                return True
            node = node.next

        return False


    def print_hash_table(self):
        for index, i in enumerate(self.table):
            node = i.head
            if not node:
                continue
            print(f"index {index}")
            while node:
                print(node.data, end=" ")
                node = node.next
            print("")
            print("----------------------------")

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next


words = []

with open("words.txt", "r") as k:
    for word in k.readlines():
        words.append(word.replace("\n", ""))

print(len(words))

hash_table = Hash_table()


# start_inserting= time.time()

# for word in words:
#     hash_table.insert(word)

# stop_inserting = time.time()

# print(f"Time inserting {stop_inserting - start_inserting}")

# start_deleting = time.time()

# hash_table.delete(words[-1])
# stop_deleting = time.time()

# print(f"Time deleting {stop_deleting - start_deleting}")

# def printMenu():
#     print("""i: insert item \n
#              d: delete item
#              n: print hashtable

#     """)

while True:
    eingabe = input("Bitte gebe eine action ein \n")

    if (eingabe == "i"):
        eingabe = input("Bitte gebe das zu speichernde wort ein \n")
        if not eingabe == "":
            hash_table.insert(eingabe)

    if (eingabe == "d"):
        eingabe = input("Bitte gebe das zu löschende Wort ein \n")
        if not eingabe == "":
            hash_table.delete(eingabe)

    if (eingabe == "n"):
        hash_table.print_hash_table()










