from AgentAlerter import *
from PersistenceAgent import *
from PiezoElectricReader import *
from MotionSensorReader import *
from WifiAntennaReader import *
import time

POLLING_PERIOD = 3

class ReadingsHUB:



    agentAlerter = None
    persistenceAgent = None
    piezoElectricReader = None
    motionSensorReader = None
    wifiAntennaReader = None

    def __init__(self):
        self.persistenceAgent = PersistenceAgent()
        self.agentAlerter = AgentAlerter(self.persistenceAgent)
        self.piezoElectricReader = PiezoElectricReader()
        self.motionSensorReader = MotionSensorReader()
        self.wifiAntennaReader = WifiAntennaReader()
        while True:
            gatheredInfo = self.pollReaders()
            alertResults = self.agentAlerter.processAndAlert(gatheredInfo)
            gatheredInfo['alertResults'] = alertResults
            self.persistenceAgent.storeRawData(gatheredInfo)
            time.sleep(POLLING_PERIOD)

    def pollReaders(self):
        result = {
            "piezo": self.piezoElectricReader.detectPresence(),
            "motion": self.motionSensorReader.detectMotion(),
            "wifi": self.wifiAntennaReader.getDetectedHosts()
        }
        return result
