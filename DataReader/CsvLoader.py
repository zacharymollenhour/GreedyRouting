import csv
import json
from HashTable import HashTable
from DataModel.Package import Package
class CsvLoader(object):
    '''
    Class Responsible for loading csv and reading in the data for both files
    '''

    def __init__(self,file):
        self.file = file
        self.rowCount = 0

    def getRowCount(self):
        for line in self.file:
            self.rowCount += 1
        return self.rowCount

    def loadPackageData(self):

        '''
        Class that handles reading in the WGUPSPackageFile.csv
        '''


        #Start by initiating a hash table for the number of rows in the package file
        hashTable = HashTable(self.getRowCount)

        #Open up the csv file
        with open(self.file) as packageFile:
            #Reset pointer
            packageFile.seek(0)


            #Initialize a csv reader object
            csvReader = csv.reader(packageFile)

            #Parse each row
            for row in csvReader:
                #Store each row into the packageData list
                key = row[0]
                packageid = row[0],
                street = row[1],
                city = row[2],
                state = row[3],
                zip = row[4],
                deadline = row[5],
                weight = row[6],
                status = 'AT HUB'
                notes = row[7]

                packagetemp = Package(packageid,street,city,state,zip,deadline,weight,status,notes)
                hashTable.insert(key, packagetemp)
            return hashTable

    def loadDistanceData(self):
        with open(self.file) as distanceCsv:
            distanceCsv.seek(0)
            distanceData = csv.reader(distanceCsv)

            rawData = []
            for row in distanceData:
                if row[0] == 9:
                    row[1] == '410 S State St.'
                    row[2] == 'Salt Lake City'
                    row[4] == 84111
                rawData.append(row)
            return rawData