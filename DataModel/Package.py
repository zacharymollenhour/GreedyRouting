from HashTable import HashTable
import csv

'''
This Class handles the outline/structure of a package object
'''

class Package:
    '''Initialize Package Object'''
    def __init__(self, packageid, street, city, state, zip, deadline, weight, delivery_status, notes):
        self.packageid = packageid
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.notes = notes

    def hashFunc(self):
        return hash(self.packageid)
