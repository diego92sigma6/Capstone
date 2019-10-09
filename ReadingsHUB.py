import AgentAlerter
import PersistenceAgent
import PiezoElectricReader
import MotionSensorReader
import WifiAntennaReader
import time

POLLING_PERIOD = 1

class ReadingsHUB:

    agentAlerter = None
    persistenceAgent = None
    piezoElectricReader = None
    motionSensorReader = None
    wifiAntennaReader = None

    def __init__(self):
        self.agentAlerter = AgentAlerter()
        self.persistenceAgent = PersistenceAgent()
        self.piezoElectricReader = PiezoElectricReader()
        self.motionSensorReader = MotionSensorReader()
        self.wifiAntennaReader = WifiAntennaReader()
        while True:
            gatheredInfo = self.pollReaders()
            self.agentAlerter.processAndAlert(gatheredInfo)
            self.persistenceAgent.storeRawData(gatheredInfo)
            time.sleep(POLLING_PERIOD)

    def pollReaders(self):
        result = {
            "piezo": self.piezoElectricReader.detectPresence(),
            "motion": self.motionSensorReader.detectMotion(),
            "wifi": self.wifiAntennaReader.getDetectedHosts()
        }
        return result
