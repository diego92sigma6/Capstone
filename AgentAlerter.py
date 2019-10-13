from CameraOperator import CameraOperator

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
        #always
        detectedPlate, picture = CameraOperator.captureAndProcess()
        print('Detected plate: %s' % (detectedPlate))
        self.storeLicensePlate(detectedPlate, picture)


    """
    Uses the persistence agent to store the taken picture + the detected license plate
    """
    def storeLicensePlate(self, detectedPlate, picture):
        self.persistenceAgent.storeLicensePlate(detectedPlate, picture)

