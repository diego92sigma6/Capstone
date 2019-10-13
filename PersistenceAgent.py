import pymongo
import datetime

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DATABASE_NAME = 'Capstone'

class PersistenceAgent:
    def __init__(self):
        self.mongoClient = None
        self.database = None
        self.prepareDatabaseConnection()
        #not implemented
        return

    """
    Initializes the database connection
    """
    def prepareDatabaseConnection(self):
        self.mongoClient = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        self.database = self.mongoClient[MONGO_DATABASE_NAME]

    def storeLicensePlate(self, detectedPlate, picture):
        if self.database is None:
            raise Exception('Expected to have an open connection to the database')
        else:
            #Prepare image (byte array)
            byteImage = picture.tobytes()

            licensePlateCollection = self.database['LicensePlates']
            licensePlateCollection.insert({
                "licensePlate": detectedPlate,
                "picture": None
            })

    """
    Prepares the data to be stored on a database
    TODO: test
    """
    def storeRawData(self, gatheredInfo):
        if self.database is None:
            raise Exception('Expected to have an open connection to the database')
        rawdataCollection = self.database['Rawdata']
        formattedInfo = self.formatInfo(gatheredInfo)
        rawdataCollection.insert_many(formattedInfo)
        return

    """
    Prepares the info with column names to be inserted in the collection
    TODO: Implement formatting
    """
    def formatInfo(self, gatheredInfo):
        result = [
            {
                "type": "motion",
                "data": gatheredInfo["motion"],
                "date": datetime.datetime.now()
            },
            {
                "type": "piezo",
                "data": gatheredInfo["piezo"],
                "date": datetime.datetime.now()
            },
            {
                "type": "wifi",
                "data": gatheredInfo["wifi"],
                "date": datetime.datetime.now()
            },
        ]
        return result

