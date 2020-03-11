import Constants
import RPi.GPIO as GPIO
import time

PIN = Constants.PIEZO_SENSOR_PIN


class PiezoElectricReader:

    def __init__(self):
        GPIO.setup(PIN, GPIO.IN)

    '''
    Detects the presence based on GPIO readings and processing
    '''

    def detectPresence(self):
        detected = self.getReading()
        print('[PIEZO] reading = %s'%(detected))
        return detected


    '''
    Processes the GPIO reading and determines if presence was detected
    '''

    def getReading(self):
        # mock return
        return GPIO.input(PIN) == 1
