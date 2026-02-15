class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key  #contact name
        self.value = value #contact object
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size=10):
        self.size = size
        self.data = [None] * self.size
   
    # Simple hash function
    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    # Insert with collision handling and duplicate update
    def insert(self, key, number):
        index = self.hash_function(key)
        new_contact = Contact(key, number)
        new_node = Node(key, new_contact)

        # If bucket is empty
        if self.data[index] is None:
            self.data[index] = new_node
            return

        # Traverse linked list
        current = self.data[index]
        while current:
            # If key already exists → update number
            if current.key == key:
                current.value.number = number
                return
            # If end reached → add new node
            if current.next is None:
                current.next = new_node
                return
            current = current.next

    # Search for a contact
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    # Print table structure
    def print_table(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")

            current = self.data[i]
            if current is None:
                print("Empty")
            else:
                while current:
                    print(current.value, end=" -> ")
                    current = current.next
                print("None")
# Test your hash table implementation here.  

table = HashTable(10)

table.insert("John", "555-1234")
table.insert("Rebecca", "111-555-0002")
table.insert("Mary", "222-1111")

table.print_table()

print("\nSearch for John:")
result = table.search("John")
print(result)

print("\nDuplicate test (update John):")
table.insert("John", "999-9999")
print(table.search("John"))