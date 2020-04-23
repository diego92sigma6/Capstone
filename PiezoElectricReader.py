'''
Author Diego Marquez

This file contains code for handling the piezoelectric sensor interrupts
Also, offers the last reading for the orchestrator
'''

import Constants
import RPi.GPIO as GPIO
import threading
import multiprocessing
import time

PIN = Constants.PIEZO_SENSOR_PIN
queue = multiprocessing.Queue(1)


class PiezoElectricReader:


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
        GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(PIN, GPIO.BOTH, bouncetime=50)
        GPIO.add_event_detect(PIN, GPIO.BOTH)
        print('[PIEZO] Started')
        self.poll()

    def poll(self):
        while True:
            print('[PIEZO] Polling')
            if GPIO.event_detected(PIN):
                self.triggerHandler()
                GPIO.remove_event_detect(PIN)
                #GPIO.add_event_detect(PIN, GPIO.BOTH, bouncetime=50)
                GPIO.add_event_detect(PIN, GPIO.BOTH)
            time.sleep(Constants.POLLING_PERIOD)


    def triggerHandler(self):
        print('[PIEZO] Triggered')
        if (queue.empty()):
            queue.put(True)

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
        if queue.empty():
            return False
        else:
            reading = queue.get()
            return reading
