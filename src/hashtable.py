# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        
        # declare variables
        temp = ''
        hashed = self._hash_mod(key)
        storage_2 = self.storage[hashed]

        # search for matching key
        while storage_2 != None and storage_2.key != key:
            temp = storage_2
            storage_2 = temp.next
        
        # check for collisions
        # if no collision, store the value with the given key
        # if a collision is found, handle with Linked List Chaining
        if storage_2 != None:
            storage_2.value = value
        else:
            linked = LinkedPair(key, value)
            linked.next = self.storage[hashed]
            self.storage[hashed] = linked
        

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # declare variables
        temp = None
        hashed = self._hash_mod(key)
        storage_2 = self.storage[hashed]

        # search for matching key
        while storage_2 != None and storage_2.key != key:
            temp = storage_2
            storage_2 = storage_2.next

        # matching key is not found
        if self.storage[hashed] == None:
            return "Can't find that key"

        # if matching key is found, remove it
        else:
            if temp == None:
                self.storage[hashed] = storage_2.next
            else:
                temp.next = storage_2.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # declare variables
        temp = ''
        hashed = self._hash_mod(key)
        storage_2 = self.storage[hashed]

        # search for value with given key
        while storage_2 != None:
            if storage_2.key == key:
                return storage_2.value
            storage_2 = storage_2.next
        
        # if not found return None
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        # declare variables
        storage_old = self.storage

        # increase capacity
        self.capacity *= 2
        self.storage = self.capacity * [None]

        # copy old hash table to new hash table
        for index in storage_old:
            temp = index
            while temp != None:
                self.insert(temp.key, temp.value)
                temp = temp.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
