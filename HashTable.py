"""
    Hash Table Class
    The Hash Table is using chaining for collisions
    We will utilize a linked list to store indexes for each element of the buckets array
    This linkedlist will provide us with key for a given index (node)
    Zachary Mollenhour WGU Student Number: 001462017
"""

'''Develop a hash table, without using any additional libraries or classes, with an insertion function that takes the following components as input and inserts the components into the hash table:
    •  package ID number
    •  delivery address
    •  delivery deadline
    •  delivery city
    •  delivery zip code
    •  package weight
    •  delivery status (e.g., delivered, in route)
'''
import csv

class Node(object):
    '''Used for storing linkedlist of nodes that contain the objects stored at each index'''
    def __init__(self, key, value):
        #self.nodeList = []
        self.key = key
        self.value = value


class HashTable:
    def __init__(self):
        '''Define the hash table size, capacity (number of elements that have been inserted), and buckets (the internal array, storing each inserted value in a bucket based on key)'''
        self.size = 0
        self.capacity = 10
        self.list = []
        #Initialize all to empty values
        for _ in range(self.capacity):
            self.list.append([])
        
    def hash(self,key):
        '''Hash Function to calculate the index where a value can be inserted into'''
        return int(key) % len(self.list)  


    def insert(self, key, value):
        '''Function that handles insertion of a node into a empty bucket (if index is empty) 
           Or if the index is not empty (collision occurred) iterate to the end of the list and add a new node there'''

        #Generate index value
        bucket = self.hash(key)

        #Set the key and value pair together for appending to list
        key_value = [key, value]

        #heck if values exist in the list for the determined index
        if self.list[bucket] == None:
            #If not we can add the value to the list at the determined index
            self.list[bucket] = list([key_value])
            return True
        else:
            #Other wise, we will find the determined index and add it to the second [1] element spot
            for pair in self.list[bucket]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True

            #Append it to the list
            self.list[bucket].append(key_value)
            return True

    def find(self, key):
        '''Function that handles the retrieving of data from the hash table'''
        bucket = self.hash(key)

        #Check if there is a item at the determined index
        if self.list[bucket] != None:
            for pair in self.list[bucket]:
                if pair[0] == key:
                    #return value of located key
                    return pair[1]
        return None

    def delete(self,key):
        '''Function used to delete a node from a linkedlist and return the nodes value'''

        #Start by computing the hash key to determine the index using hashFunction
        bucket = self.hash(key)

        #Check if the list contains any elements at the index
        if self.list[bucket] is None:
            return False

        #Otherwise, loop through the range of the length of the list at given bucket
        for i in range(0, len(self.list[bucket])):
            #Look for key that was passed in 
            if self.list[bucket][i][0] == key:
                #delete the value for passed in key
                self.list[bucket].pop(i)
                return True
        return False

def readCSVData(filepath):
    '''We must create a object of above class and read in the WGUPS Package File'''

    #Create a HashTable Class Object
    packageObject = HashTable()

    #Open Excel File and read in content
    with open(filepath) as WGUPackageFile:
        #Initiate a csv reader instance
        package_data = csv.reader(WGUPackageFile)

        #Automatically skip the header of the file
        next(package_data, None)

        #Loop through each row and read data into a list
        for item in package_data:
            #First inserts the package id item[0] and then the remainding data (all of package data)
            packageObject.insert(int(item[0]), item)
    print(packageObject.find(10))
    #print(packageObject.find(10))
    #if(packageObject.find(10) != None):
        #print("WOW")
    #Return Object
    return packageObject

#Call readCSVData Function with given package name
readCSVData("WGUPSPackageFile.csv")

#Hashtable
