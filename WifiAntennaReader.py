import os
import subprocess
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import threading
import re
import numpy as np
from datetime import *
from Constants import POLLING_PERIOD

class WifiReading:
    bssid = None
    pwr = None
    beacons = None
    data = None
    rate = None
    channel = None
    mb = None
    enc = None
    auth = None
    essid = None
    #created = None

    def __init__(self, bssid, pwr, beacons, data, rate, channel, mb ,enc, cipher, auth, essid):
        self.bssid = bssid
        self.pwr = int(pwr)
        self.beacons = int(beacons)
        self.data = int(data)
        self.rate = int(rate)
        self.channel = int(channel)
        self.mb = mb
        self.enc = enc
        self.cipher = cipher
        self.auth = auth
        self.essid = essid
        self.created = datetime.now()

ANTENNA0 = 'wlan1'
ANTENNA1 = 'wlan2'

"""
Will use the library called pycrack, which is an
interface to the airmon-ng toolset for Wifi Detection
"""
class WifiAntennaReader:

    pollingThread = None
    antenna0 = []
    antenna1 = []

    def configure_antenna(self, antennaName):
        subprocess.call(['sudo','ifconfig',antennaName, 'down'])
        subprocess.call(['sudo','iwconfig',antennaName, 'mode', 'monitor'])
        subprocess.call(['sudo','ifconfig',antennaName, 'up'])

    
    def __init__(self):


        # prepare monitor mode
        # run the shell as a subprocess:
        p0 = subprocess.Popen(['sudo', 'airodump-ng', ANTENNA0], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        p1 = subprocess.Popen(['sudo', 'airodump-ng', ANTENNA1], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        # set the O_NONBLOCK flag of p.stdout file descriptor:
        flags = fcntl(p0.stdout, F_GETFL) # get current p.stdout flags
        flags = fcntl(p1.stdout, F_GETFL) # get current p.stdout flags
        fcntl(p0.stdout, F_SETFL, flags | O_NONBLOCK)
        fcntl(p1.stdout, F_SETFL, flags | O_NONBLOCK)


        self.pollingThread = threading.Thread(target = self.pollAntennas, args = (p0, p1,))
        self.pollingThread.daemon = True
        self.pollingThread.start()


    def pollAntennas(self, p0, p1):
        # let the shell output the result:
        # get the output
        while True:
            sleep(POLLING_PERIOD)
            print('[WIFI] Polling antennas async')
            try:
                self.formatAntennaData(read(p0.stderr.fileno(), 1024*2**4).decode("utf-8"), antennaNumber = 0)
                self.formatAntennaData(read(p1.stderr.fileno(), 1024*2**4).decode("utf-8"), antennaNumber = 1)
            except OSError:
                # the os throws an exception if there is no data
                print ('[No more data]')
                continue

    def formatAntennaData(self, readingString, antennaNumber):

        if len(readingString) == 0:
            return
        lines = [line.split() for line in readingString.split('\n') if re.compile(r'.*([\d\w]{2}:){5}[\d\w]{2}').match(line)]
        readings = [WifiReading(*l) for l in lines if len(l) == 11 if not np.any([re.compile(r'.*associated.*').match(col) for col in l])]
        antenna = self.antenna0 if antennaNumber == 0 else self.antenna1
        oneMinuteAgo = datetime.now() - timedelta(minutes = 1)
        for reading in readings:
            self.addAntennaData(reading, antenna)
            if (reading.created < oneMinuteAgo):
                readings.remove(reading)


    '''
    Adds data to the antenna array
    '''
    def addAntennaData(self, reading, antenna):
        lastReading = [storedReading for storedReading in antenna if storedReading.bssid == reading.bssid]
        oneMinuteAgo = datetime.now() - timedelta(minutes = 1)

        if len(lastReading) is 0:
            antenna.append(reading)
        elif lastReading[0].created < oneMinuteAgo:
            antenna.remove(lastReading[0])
            antenna.append(reading)
        return antenna



    """
    Uses the antenna to detect hosts as an independent access point
    The intensity will later be used as a feature in the predictive model
    :return a paired list of phones + signal intensity
    """
    def getDetectedHosts(self):
        readings = self.getAirmonReadings()
        #phoneIntensityPairs = self.formatReadings(readings)
        return readings

    """
    Operates the pycrack library to get info on the hosts
    """
    def getAirmonReadings(self):
        

        out0 = self.antenna0;
        out1 = self.antenna1;

        return {
                'antenna0' : out0,
                'antenna1' : out1,
                }
        

    """
    Retrieves only the important data (mac addresses and signal intensity),
    in a Nx2 array
    """
    def formatReadings(self, readings):
        result = []
        #Implementation will change depending on how the info is obtained from pycrack
        for reading in readings:
            result.append([reading[0],reading[1]])
        return result
