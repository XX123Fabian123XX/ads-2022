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
        for i in range(103): # Orig: 53 -> 101 smallest where it still works, 103 so we can insert some more
            self.table.append(None)


    def insert(self, value):
        """ 
        insert a value into the hash table
        """

        hash_value = hash(value)
        orig_value = hash_value

        if self.is_in_table(value):
            print("ist schon in der tablele")
            return

        newIdx = 1
        while(self.table[hash_value] != None):
            hash_value = (orig_value + newIdx**2) % len(self.table)
            newIdx+=1
            if(newIdx == len(self.table)):
                print("tabelle voll!")
                return

        self.table[hash_value] = value
    
    def delete(self, value):
        """
        deletes a value out of the hash table, if it exists
        """
        if not self.is_in_table(value):
            print("Das Element gibt es nicht in der tablele")
            return 


        hash_value = hash(value)
        idx = self.find_element(value)
        if(idx == -1):
            print("Das Element gibt es nicht in der tablele")
            return

        if(self.has_chain(value)):
            lastValue = hash_value
            newIdx = 0
            while(self.table[lastValue] != None):
                lastValue = (hash_value + newIdx**2) % len(self.table)
                newIdx+=1
                if(newIdx == len(self.table)):
                    break

            # subtract 2 to get the last "real" idx with a value
            lastValue = (hash_value + (newIdx-2)**2) % len(self.table)

            if(lastValue == idx):
                self.table[idx]
            self.table[idx] = self.table[lastValue]
            self.table[lastValue] = None
        else:
            self.table[idx] = None


    def is_in_table(self, value):
        return self.find_element(value) != -1

    def find_element(self, value):
        hash_value = hash(value)
        orig_value = hash_value
        newIdx = 1


        while(self.table[hash_value] != None):
            if self.table[hash_value] == value:
                return hash_value
            hash_value = (orig_value + newIdx**2) % len(self.table)
            newIdx+=1
            if(newIdx == len(self.table)):
                return -1
            
        return -1

    def get_newIdx(self, value):
        hash_value = hash(value)
        orig_value = hash_value
        newIdx = 1


        while(self.table[hash_value] != None):
            if self.table[hash_value] == value:
                return newIdx
            hash_value = (orig_value + newIdx**2) % len(self.table)
            newIdx+=1
            if(newIdx == len(self.table)):
                return -1
            
        return -1

    def has_chain(self,value):
        hash_value = hash(value)
        orig_value = hash_value
        newIdx = 1

        if self.table[hash_value] == None:
            return False
        new_value = (hash_value + 1) % len(self.table)
        if self.table[new_value] == None:
            return False
        if hash(self.table[new_value]) != hash(value):
            return False

        return True


    def print_hash_table(self):
        for index, i in enumerate(self.table):
            value = i
            if not value:
                continue
            print(f"index {index}: value \"{value}\"")
            print("----------------------------")

words = []

with open("words.txt", "r") as k:
    for word in k.readlines():
        words.append(word.replace("\n", ""))

print(len(words))

hash_table = Hash_table()

start_inserting= time.time()

for word in words:
    hash_table.insert(word)

stop_inserting = time.time()

print(f"Time inserting {stop_inserting - start_inserting}")

start_deleting = time.time()

hash_table.delete(words[-1])
stop_deleting = time.time()

print(f"Time deleting {stop_deleting - start_deleting}")

def printMenu():
    print("""i: insert item \n
             d: delete item
             n: print hashtable

    """)

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










