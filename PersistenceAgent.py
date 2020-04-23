'''
Author Diego Marquez

This file handles the data storge into a mongo database
pictures are saved using GridFS, a special subsystem of Mongo
dedicated to storing blobs
'''

import pymongo
import datetime
import gridfs
import base64
from bson import json_util
import json

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
            
            b64 = base64.b64encode(picture)
            pictureID = self.fs.put(b64, encoding='utf-8')
            licensePlateCollection = self.database['LicensePlates']
            licensePlateCollection.insert({
                "licensePlate": detectedPlate,
                "pictureID": pictureID,
                "date": datetime.datetime.now()
            })
            print('[PERSISTENCE] stored picture id: %s' % (pictureID))

            return {
                    'pictureID'  : pictureID,
                    #'shape' : picture.shape,
                    #'dtype': str(picture.dtype)
                    }

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
        antennas =  gatheredInfo['wifi']
        antenna0 = [json.dumps(reading.__dict__, default=str) for reading in antennas['antenna0']]
        antenna1 = [json.dumps(reading.__dict__, default=str) for reading in antennas['antenna1']]
        wifi = [antenna0, antenna1]
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
                "data": wifi,
                "date": now
            },
        ]
        if gatheredInfo['alertResults'] is not None:
            if gatheredInfo['alertResults']['pictureID'] is not None:
                result.append({
                    "type": "camera",
                    "data": gatheredInfo['alertResults']['pictureID'],
                    "date": now,
                    #"shape": gatheredInfo['alertResults']['shape'],
                    #"dtype": gatheredInfo['alertResults']['dtype'],
                })
        return result

