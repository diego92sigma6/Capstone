from CameraOperator import CameraOperator
from DashboardSocketServer import update_dashboard_info
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import sys
import threading
from math import isnan
from sklearn.ensemble import RandomForestRegressor

HEADERS = [
'Piezo', 
'Motion', 
'Antenna 0 readings', 
'Antenna 1 readings', 
'Antenna 0 average power', 
'Antenna 1 average power',
'Antenna 0 median power', 
'Antenna 1 median power', 
'Antenna 0 std deviation', 
'Antenna 1 std deviation'] + ['antenna 0 reading %d'%(i) for i in range(0, 100)] + ['antenna 1 reading %d'%(i) for i in range(0, 100)] + ['Amount Of Cars']

TRAINING_MODE = True
CURRENT_AMOUNT_OF_CARS = 1

class AgentAlerter:

    lastPicture = None

    def __init__(self, persistenceAgent):
        if persistenceAgent is None:
            raise Exception('Expected a persistence agent to store information')
        else:
            self.persistenceAgent = persistenceAgent
        

    """
    Will determine if the data corresponds to an event that should be raised.
    TODO: Implement regression model here
    """
    def processAndAlert(self, gatheredInfo):

        self.addDataToDataset(gatheredInfo)
        #Determine detected cars using all readings

        if gatheredInfo['motion'] == 1 and gatheredInfo['piezo'] == 1:
            detect = threading.Thread(target=self.detectLicensePlate)
            detect.start()
            return self.lastPicture
        else:
            return None

    def detectLicensePlate(self):
        detectedPlate = None
        picture = None
        detectedPlate, picture = CameraOperator.captureAndProcess()
        if detectedPlate is not None or picture is not None:
            print('[ALERTER] Detected plate: %s' % (detectedPlate))
            pictureMetadata = self.storeLicensePlate(detectedPlate, picture)
            self.lastPicture = pictureMetadata            
        else:
            print('[ERROR] no detected plate')

    def addDataToDataset(self, readings):
        with open('trainingData.csv', 'a+') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            length = 0
            for row in reader:
                length += 1
            if length == 0:
                headersRow = HEADERS
                writer.writerow(headersRow)
            antenna0 = readings['wifi']['antenna0']
            antenna1 = readings['wifi']['antenna1']
            a0pwr = np.array([reading.pwr for reading in antenna0])
            a1pwr = np.array([reading.pwr for reading in antenna1])
            newRow = np.array([])
            newRow = np.append(newRow, readings['piezo'])
            newRow = np.append(newRow, readings['motion'])
            newRow = np.append(newRow, len(antenna0))
            newRow = np.append(newRow, len(antenna1))
            newRow = np.append(newRow, np.average(a0pwr) if not isnan(np.average(a0pwr)) else 0)
            newRow = np.append(newRow, np.average(a1pwr) if not isnan(np.average(a1pwr)) else 0)
            newRow = np.append(newRow, np.median(a0pwr) if not isnan(np.median(a0pwr)) else 0)
            newRow = np.append(newRow, np.median(a1pwr) if not isnan(np.median(a1pwr)) else 0)
            newRow = np.append(newRow, np.var(a0pwr) if not isnan(np.var(a0pwr)) else 0)
            newRow = np.append(newRow, np.var(a1pwr) if not isnan(np.var(a1pwr)) else 0)

            #create readings
            padded0 = np.zeros(100)
            padded1 = np.zeros(100)
            padded0[:a0pwr.shape[0]] = sorted(a0pwr, reverse=True)
            padded1[:a1pwr.shape[0]] = sorted(a1pwr, reverse=True)

            newRow = np.append(newRow, padded0)
            newRow = np.append(newRow, padded1)

            if TRAINING_MODE:
                newRow = np.append(newRow, CURRENT_AMOUNT_OF_CARS)
            else:
                estimatedAmountOfCars = self.predictAmountOfCars(newRow)
                newRow = np.append(newRow, estimatedAmountOfCars)  
            
            #save row
            writer.writerow(newRow)
            #emit new row
            update_dashboard_info(newRow)


    def predictAmountOfCars(self, testData):
        try:
            dataset = pd.read_csv('trainingData.csv', delimiter=',' )
            X = dataset.iloc[:, 1:(len(HEADERS))].values
            Y = dataset.iloc[:, len(HEADERS)-1].values
            regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
            regressor.fit(X,Y)
            testData.reshape(-1, 1)
            y_pred = regressor.predict(np.reshape(testData, (1, -1)))
            return y_pred[0]
        except Error:
            print('[REGRESSION] Error:')
            print(Error)
            return -1




    """
    Uses the persistence agent to store the taken picture + the detected license plate
    """
    def storeLicensePlate(self, detectedPlate, picture):
        return self.persistenceAgent.storeLicensePlate(detectedPlate, picture)

