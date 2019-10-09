"""
Will use the library called pycrack, which is an
interface to the airmon-ng toolset for Wifi Detection
"""
class WifiAntennaReader:

    """
    Uses the antenna to detect hosts as an independent access point
    The intensity will later be used as a feature in the predictive model
    :return a paired list of phones + signal intensity
    """
    def GetAmountOfDetectedHosts(self):
        readings = self.getAirmonReadings()
        phoneIntensityPairs = self.formatReadings(readings)
        return phoneIntensityPairs

    """
    Operates the pycrack library to get info on the hosts
    """
    def getAirmonReadings(self):
        #mock data
        return [['00:00:00:00:00:00', -90, 'other info'],
                ['00:00:00:00:00:01', -80, 'other info'],
                ['00:00:00:00:00:02', -85, 'other info'],
                ['00:00:00:00:00:03', -89, 'other info'],
                ['00:00:00:00:00:04', -81, 'other info'],
                ['00:00:00:00:00:05', -50, 'other info']]

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