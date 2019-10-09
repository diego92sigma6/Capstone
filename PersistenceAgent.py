import pymongo

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

    """
    Prepares the data to be stored on a database
    TODO: test
    """
    def storeRawData(self, gatheredInfo):
        if self.database is None:
            raise Exception('Expected to have an open connection to the database')
        rawdataCollection = self.database['Rawdata']
        formattedInfo = self.formatInfo(gatheredInfo)
        rawdataCollection.insertMany(formattedInfo)
        return

    """
    Prepares the info with column names to be inserted in the collection
    TODO: Implement formatting
    """
    def formatInfo(self, gatheredInfo):
        #not implemented
        return gatheredInfo

