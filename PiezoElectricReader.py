import Constants
import RPi.GPIO as GPIO
import threading
import multiprocessing
import time

PIN = Constants.PIEZO_SENSOR_PIN


class PiezoElectricReader:

    sensor_was_touched = False

    def __init__(self):
        print('[PIEZO] Starting piezo reader')
        #self.sensorThread = threading.Thread(target = self.waitForSensor)
        #self.sensorThread.daemon = True
        #self.sensorThread.start()
        self.sensorProcess = multiprocessing.Process(target = self.waitForSensor)
        self.sensorProcess.start()

    '''
    Process that waits for interrupt
    '''
    def waitForSensor(self):
        GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(PIN, GPIO.BOTH, bouncetime=50)
        print('[PIEZO] Started')
        self.poll()

    def poll(self):
        while True:
            print('[PIEZO] Polling')
            if GPIO.event_detected(PIN):
                self.triggerHandler()
                GPIO.remove_event_detect(PIN)
                GPIO.add_event_detect(PIN, GPIO.BOTH, bouncetime=50)
            time.sleep(Constants.POLLING_PERIOD)


    def triggerHandler(self):
        print('[PIEZO] Triggered')
        self.sensor_was_touched = True


    '''
    Detects the presence based on GPIO readings and processing
    '''
    def detectPresence(self):
        detected = self.getReading()
        if detected:
            #Make sure to turn off the detected state
            #Another interrupt shall turn it on the next time
            self.sensor_was_touched = False
        print('[PIEZO] reading = %s'%(detected))
        return detected


    '''
    Processes the GPIO reading and determines if presence was detected
    '''

    def getReading(self):
        # mock return
        return self.sensor_was_touched
