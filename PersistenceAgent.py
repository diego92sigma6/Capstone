import pymongo
import datetime
import gridfs

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DATABASE_NAME = 'Capstone'

class PersistenceAgent:

    
    def __init__(self):
        self.mongoClient = None
        self.database = None
        self.fs = None
        self.prepareDatabaseConnection()
        return

    """
    Initializes the database connection
    """
    def prepareDatabaseConnection(self):
        self.mongoClient = pymongo.MongoClient(MONGO_CONNECTION_STRING)
        self.database = self.mongoClient[MONGO_DATABASE_NAME]
        print(gridfs)
        self.fs = gridfs.GridFS(self.database)
        print(self.fs)

    def storeLicensePlate(self, detectedPlate, picture):
        if self.database is None:
            raise Exception('Expected to have an open connection to the database')
        elif self.fs is None:
            raise Exception('Expected to have an associated gridfs object')
        else:
            
            pictureID = self.fs.put(picture.tostring(), encoding='utf-8')

            licensePlateCollection = self.database['LicensePlates']
            licensePlateCollection.insert({
                "licensePlate": detectedPlate,
                "pictureID": pictureID,
                "date": datetime.datetime.now()
            })

            return pictureID

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
        now = datetime.datetime.now()
        result = [
            {
                "type": "motion",
                "data": gatheredInfo["motion"],
                "date": now
            },
            {
                "type": "piezo",
                "data": gatheredInfo["piezo"],
                "date": now
            },
            {
                "type": "wifi",
                "data": gatheredInfo["wifi"],
                "date": now
            },
        ]
        return result

