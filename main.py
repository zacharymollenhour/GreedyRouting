from DataReader.CsvLoader import CsvLoader
from HashTable import HashTable



def createPackageHashTable():
    """
    Function that passes the package data csv file to the file reader class
    Creates a hash table based off hte size
    Constucts and fills hash table with data
    """

    packageData = CsvLoader('WGUPSPackageFile.csv')
    fileSize = packageData.getRowCount()
    packagehashTable = HashTable(fileSize)
    packagehashTable = packageData.loadPackageData()
    return packagehashTable

packageHashTable = createPackageHashTable()
print(packageHashTable.find(1))