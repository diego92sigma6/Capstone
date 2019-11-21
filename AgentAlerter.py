from CameraOperator import CameraOperator
from time import sleep
import sys

class AgentAlerter:


    def __init__(self, persistenceAgent):
        if persistenceAgent is None:
            raise Exception('Expected a persistence agent to store information')
        else:
            self.persistenceAgent = persistenceAgent
        return

    """
    Will determine if the data corresponds to an event that should be raised.
    TODO: Implement regression model here
    """
    def processAndAlert(self, gatheredInfo):
        if gatheredInfo['motion'] == 1 and gatheredInfo['piezo'] == 1:
            #always
            detectedPlate = None
            picture = None
            #try:
                #detectedPlate, picture = CameraOperator.captureAndProcess()
            #except:
                #sleep(0.1)
                ##self.processAndAlert(gatheredInfo)
                #print('failed to obtain license plate')
                #print(sys.exc_info()[0])
            detectedPlate, picture = CameraOperator.captureAndProcess()
            if detectedPlate is not None or picture is not None:
                print('[ALERTER] detectedPLate:')
                print('[ALERTER] Detected plate: %s' % (detectedPlate))
                pictureMetadata = self.storeLicensePlate(detectedPlate, picture)

                return pictureMetadata            
            else:
                print('[ERROR] no detected plate')
                return None
        else:
            return None

    """
    Uses the persistence agent to store the taken picture + the detected license plate
    """
    def storeLicensePlate(self, detectedPlate, picture):
        return self.persistenceAgent.storeLicensePlate(detectedPlate, picture)

