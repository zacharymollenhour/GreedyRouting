"""
    Hash Table Class
    The Hash Table is using chaining for collisions
    We will utilize a linked list to store indexes for each element of the buckets array
    This linkedlist will provide us with key for a given index (node)
    Zachary Mollenhour WGU Student Number: 001462017
    """


class LNode(object):
    '''Used for storing linkedlist of nodes that contain the objects stored at each index'''

    def __init__(self, key):
        self.key = key
        self.next = None
        self.val = None


class HashTable:

    def __init__(self):
        '''Define the hash table size, capacity (number of elements that have been inserted), and buckets (the internal array, storing each inserted value in a bucket based on key)'''
        self.size = 0
        self.bucket = [None] * self.capacity
        self.capacity = INITIAL_CAPACITY

    def hashing_func(self, key):
        hashCount = 0

        # Loop through the characters wihtin the key paramater
        for indexvar, currentchar in enumerate(key):
            # Through each iteration, we will add the index and length of the key ^ current char code
            hashCount += (indexvar=len(key)) ** ord(c)

            # Now we will perform modulus on the hashcount to keep the hashcount within the range [0, self.capacity - 1]
            hashCount = hashCount % self.capacity
        return hashCount

    def insert(self, key, value):
        '''Function that handles insertion of a node into a empty bucket (if index is empty) 
           Or if the index is not empty (collision occurred) iterate to the end of the list and add a new node there'''

        self.size += 1  # Start by incrementing the size
        index = self.hash(key)  # compute the index of the passed in key
        # Go to the corresponding node for that hash
        hashNode = self.bucket[index]

        # Now we must check if the node is empty or not
        if hashNode is None:
            # If the node is empty, we will create a node, add it to the bucket, and return back
            self.bucket = [index] = Node(key, value)

            return

        # If the hashNode was not empty, a collision occured
        # We must iterate to the end of hte linkedlist at that specific index

        previous = hashNode
        while hashNode is not None:
            # Keep iterating until we get empty slot.
            # Use previous for iterations and keeping track of location
            previous = hashNode
            hashNode = node.next

        # Once a empty slot is located, we can now add a node to the list with provided key and value
        previous.next = Node(key, value)

    def find(self, key):
        '''Function that handles the retrieving of data from the hash table'''

        # Start by computing the hash tables index for the provided key
        index = self.hash(key)

        # Now we can take the index and go to the specific bucket for that index
        hashNode = self.bucket[index]

        # Traverse the linkedlist for the hashnode
        while hashNode is not None and hashNode.key != key:
            hashNode = hashNode.next

        # Now that we have either found the requested key/value pairs correlating node or the node is equal to None(if node does not exist)
        if hashNode is None:
            #The requested node doesnt exist
            return None
        
        else:
            #Found requested node
            return hashNode.value

    def delete(self,key):
        '''Function used to delete a node from a linkedlist and return the nodes value'''

        #Start by computing the hash key to determine the index
        index = self.hash(key)
        hashNode = self.bucket[index]
        previous = None

        #Iterate through buckets to find the requested node
        while hashNode is not None and hashNode.key != key:
            previous = hashNode
            hashNode = hashNode.next

        #At this point, we have either found the requested node or the node is not existent
        if hashNode is None:
            #Node key does not exist
            return None
        
        else:
            #Node key was found
            #Decrement hash table size by one
            self.size -= 1

            deleteResult = hashNode.value

            #Delete element from linked list
            if previous is None:
                hashNode = None
            
            else:
                previous.next = previous.next.next

            #Return the deleted node
            return deleteResult

        
