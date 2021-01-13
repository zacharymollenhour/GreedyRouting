import csv
import datetime

class Distance:
    '''Initialize Distance Object'''
    def __init__(self, rawData):
        self.rawData = rawData
        self.distancesTable = []
        self.keylabels = []

    def prepData(self):
        """
        Function that prepares the distance data
        Starts by retrieving the keylabel (first row of data in csv)
        Then we will organize all raw data into a clean list wiht no blank spots
        Once we have keys set we can utilize those for finding hte distance
        """

        self.keylabels = self.rawData.pop(0)

        #Clean and remove empty keylabels
        for item in self.keylabels:
            if item == '':
                self.keylabels.remove(item)
            
        #prepare a counter 
        counterVar = len(self.rawData) - 1

        while len(self.rawData) != 0:
            removedData = self.rawData.pop(0)
            temp_keylist = []
            subKeyVal = []

            labelCounter = 0
            for i in removedData:
                if i == removedData[0]:
                    temp_keylist = i
            
                else:
                    subKeyVal = self.keylabels[labelCounter]
                    tempDistance = i

                    tempSubKey = subKeyVal, tempDistance

                    subKeyVal.append(list(tempSubKey))
                    subKeyVal += 1

                if labelCounter == len(self.keylabels) - 1:
                    keyvaluepair = temp_keylist, subKeyVal
                    self.distancesTable.append(list(keyvaluepair))
            
            counterVar -= 1
        return self.distancesTable

    def getkeyLabels(self):
        return self.keylabels