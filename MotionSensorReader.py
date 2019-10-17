import Constants as Constants
import RPi.GPIO as GPIO

class MotionSensorReader:

    def __init__(self):
	GPIO.setup(11, GPIO.IN)
	GPIO.setup(3, GPIO.OUT)


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
	reading = GPIO.input(Constants.MOTION_SENSOR_PIN)
	print('motion sensor = %s'%(reading))
	if reading == 1:
		GPIO.output(Constants.MOTION_SENSOR_LED_PIN, 1)
	else:
		GPIO.output(Constants.MOTION_SENSOR_LED_PIN, 0)
        return reading

    '''
    Processes the reading obtained by the GPIO pin and determines whether
    it corresponds to a detected car
    '''

    def determineMotionDetection(self, motionSensorReading):
	return motionSensorReading == 1
