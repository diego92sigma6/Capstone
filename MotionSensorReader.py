class MotionSensorReader:

    """
    Orchestrates the readings from the sensor
    """
    def detectMotion(self):
        motionSensorReading = self.readFromMotionSensorPin()
        detectionOccured = self.determineMotionDetection(motionSensorReading)
        return detectionOccured

    '''
    The motion sensor has built in digital logic that outputs either a 3v3 or 0,
    depending on whether motion was detected by it 
    '''

    def readFromMotionSensorPin(self):
        # mock data
        return 1

    '''
    Processes the reading obtained by the GPIO pin and determines whether
    it corresponds to a detected car
    '''

    def determineMotionDetection(self, motionSensorReading):
        # mock data
        return True
