import os
import subprocess
from time import sleep
from fcntl import fcntl, F_GETFL, F_SETFL
from os import O_NONBLOCK, read
import threading

if __name__ == "__main__":
    reader = new WifiAntennaReader()

"""
Will use the library called pycrack, which is an
interface to the airmon-ng toolset for Wifi Detection
"""
class WifiAntennaReader:

    pollingThread = None
    antenna0 = None
    antenna1 = None
    
    def __init__(self):
        # run the shell as a subprocess:
        p0 = subprocess.Popen(['sudo', 'airodump-ng', 'mon0'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        p1 = subprocess.Popen(['sudo', 'airodump-ng', 'mon1'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
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
            sleep(1)
            print('[WIFI]Polling antennas async')
            try:
                self.antenna0 =  (read(p0.stderr.fileno(), 1024).decode("utf-8"))[1:]
                self.antenna1 =  (read(p1.stderr.fileno(), 1024).decode("utf-8"))[1:]
            except OSError:
                # the os throws an exception if there is no data
                print ('[No more data]')
                continue


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
        print(out0)

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
